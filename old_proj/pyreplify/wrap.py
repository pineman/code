#!/bin/env python3
"""
Run a python script line by line on the REPL
"""

import os
import sys
import signal
import tty
import termios
import pty
import argparse
import re
from itertools import zip_longest


# Hardcode the prompts to their defaults
PS1 = '>>> '
PS2 = '... '
PROMPT_READY = "__import__('sys').ps1 = '{}'; \
                __import__('sys').ps2 = '{}'\n".format(PS1, PS2).encode()


def isspace(string):
    return string != '\n' and string.isspace()


def remove_last_prompt(evald):
    nl_index = evald.rfind('\n')
    if nl_index == -1:
        # evald contain just the prompt, don't print anything
        return ''
    # Remove the last prompt from the evald
    return evald[:evald.rfind('\n')]


def read_until_prompt(python, last=False):
    prompt_ready = False

    while not prompt_ready:
        evald = python.read(1024).decode()
        if evald.endswith(PS1) or evald.endswith(PS2):
            prompt_ready = True
            if last:
                evald = remove_last_prompt(evald)
        print(evald, end='')


def main(options):
    # Fork to a new pseudo-terminal and get a file descriptor to
    # read/write to its stdio
    pid, python = pty.fork()

    if pid != 0:
        python_script = options.script

        # Disable terminal input echo
        tty.setraw(python, termios.TCSANOW)
        python = os.fdopen(python, 'r+b', buffering=0)

        # Read the interpreter's first three lines
        for _ in range(3):
            data = python.readline().decode()
            if not options.quiet:
                print(data, end='')

        # Next comes the first prompt, don't write it back to the
        # real terminal just yet
        data = python.read(1024).decode()
        # Change the PS1 and PS2 of the interpreter
        python.write(PROMPT_READY)

        # Change all occurrences of more than one newline to just one.
        script = python_script.readlines()
        for i, (line, prev_line) in enumerate(zip(script, [''] + script[:-1])):
            if re.search(r'^\s*\n$', line):
                if isspace(prev_line[0]):
                    script[i] = ' \n'
                else:
                    script[i] = '\n'

        for line, prev_line in zip_longest(script, [' '] + script[:-1], fillvalue=' '):
            # If we're coming back to zero indent, i.e. to the PS1 prompt,
            # we need an extra '\n' for python to terminate the indent block.
            if not isspace(line[0]) and isspace(prev_line[0]):
                # TODO: Bug inside string literals: extra '\n' when unneeded.
                # Idea: only fix if outside string literals (detect by parse)
                python.write(b'\n')
                read_until_prompt(python, True)

            # TODO: Bug when the above read_until_prompt reads two prompts:
            # the one it's supposed to read and absorb, and the next one,
            # causing this call below to get stuck.
            # Display the results of the previous eval and a new prompt
            read_until_prompt(python)

            # Is the line a comment?
            if re.search(r'^\s*#', line):
                # Echo it to stdout but don't feed it to python.
                print(line, end='')
                python.write(b'\n')
                continue

            # Write the code to python to interpret it
            python.write(line.encode())

            # Echo it back as if the user typed it on the keyboard
            print(line, end='')


        # Display the results of the last eval.
        read_until_prompt(python, True)

        # One more newline and kill python
        os.kill(pid, signal.SIGTERM)

    else:
        # Child
        # Execute python and that's it.
        os.execl(sys.executable, sys.executable)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]),
                                     description=__doc__)

    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help="Suppress the python REPL's headers")

    parser.add_argument('script', default=sys.stdin, nargs='?',
                        type=argparse.FileType('r'),
                        help='The script to run, defaults to stdin')

    main(parser.parse_args())
