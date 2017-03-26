#!/usr/bin/env python3
# vim: ts=4 sts=4 sw=4 et

"""
Tool to merge two files by their different lines.

No, I didn't know comm(1) at the time... Archived.
This program is:
$ cp FILE1 OUTFILE && comm -13 FILE1 FILE2 >> OUTFILE
"""

from sys import argv


def diffcat(f1, f2, out):
    with open(f1, 'r') as file1:
        lines1 = file1.readlines()

    with open(f2, 'r') as file2:
        lines2 = file2.readlines()

    with open(out, 'a+') as out_file:
        for line in lines1:
            out_file.write(line)

        for line2 in lines2:
            for line1 in lines1:
                if line1 == line2:
                    break
            else:
                out_file.write(line2)


def usage():
    print('Usage: diffcat.py [FILE1] [FILE2] [OUTFILE]')
    print('concatenate FILEs, removing duplicate lines, to OUTFILE')


def main():
    try:
        f1 = argv[1]
        f2 = argv[2]
        out = argv[3]
        diffcat(f1, f2, out)
    except IndexError:
        usage()


if __name__ == "__main__":
    main()
