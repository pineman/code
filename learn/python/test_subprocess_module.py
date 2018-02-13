#!/usr/bin/env python3

import subprocess
import sys
import os


def check_output(arg):
    print("subprocess.check_output():")

    # How to subprocess.check_output()
    try:
        out = subprocess.check_output(['ls', arg], stderr=subprocess.STDOUT,
                                    universal_newlines=True)
        if out:
            print('\tstdout says:\n{0}'.format(out))
        else:
            print("\tthere's no stdout!")

        print('\tReturn code is zero.')
        sys.exit(0)

    except subprocess.CalledProcessError as error:
        print("\tPython error occurred: '{0}'".format(error))
        if error.output:
            print('\tstderr says:\n{0}'.format(error.output))
        else:
            print("\tthere's no stderr!")
        print('\tReturn code is non-zero.')
        sys.exit(error.returncode)


def popen(arg):
    print("subprocess.Popen():")

    # How to subprocess.Popen()
    proc = subprocess.Popen(['ls', arg], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, universal_newlines=True)

    out, err = proc.communicate()

    if out:
        print('\tstdout says:\n{0}'.format(out))
    else:
        print("\tthere's no stdout!")

    if err:
        print('\tstderr says:\n{0}'.format(err))
    else:
        print("\tthere's no stderr!")

    if proc.returncode:
        print('\tReturn code is non-zero.')
    else:
        print('\tReturn code is zero.')
    sys.exit(proc.returncode)


def versus(arg):
    print('Formatting differences\n') # os.system runs a shell, subprocess doesn't.

    print('os.system:')
    os.system('ls ' + arg)
    print("")

    #print(check_output(arg).decode('utf-8'))
    print(popen(arg).decode('utf-8'))


def main():
    try:
        function, arg = sys.argv[1], sys.argv[2]

        if function == 'check_output':
            check_output(arg)
        elif function == 'popen':
            popen(arg)
        elif function == 'versus':
            versus(arg)
        else:
            print("FUNCTION is one of 'check_output', 'popen', 'versus'")

    except IndexError:
        print("""\
usage: <thisscript> FUNCTION DIR
where FUNCTION is what to test:
    'check_output' -> subprocess.check_output()
    'popen' -> subprocess.Popen()
    'versus' -> os.system() vs subprocess.check_output()
and DIR is the argument to pass to ls(1)""")


if __name__ == '__main__':
    main()
