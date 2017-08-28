#!/usr/bin/env python3
# vim: ts=4 sts=4 sw=4 et

"""
Tool to merge two files by their different lines.

No, I didn't know comm(1) at the time... Archived.
This program is:
$ cp FILE1 OUTFILE && comm -13 FILE1 FILE2 >> OUTFILE
"""

from sys import argv


def diffcat(filename1, filename2, outname):
    with open(filename1, 'r') as file1:
        lines1 = file1.readlines()

    with open(filename2, 'r') as file2, open(outname, 'a+') as out_file:
        for line2 in file2:
            if line2 not in lines1:
                out_file.write(line2)


def usage():
    print('Usage: diffcat.py [FILE1] [FILE2] [OUTFILE]')
    print('concatenate FILEs, removing duplicate lines, to OUTFILE')


def main():
    try:
        filename1 = argv[1]
        filename2 = argv[2]
        outname = argv[3]
        diffcat(filename1, filename2, outname)
    except IndexError:
        usage()


if __name__ == "__main__":
    main()
