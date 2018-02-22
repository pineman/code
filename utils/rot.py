#!/usr/bin/env python3

import sys

S = "".join([l for l in open(sys.argv[1], 'r')])

for j in range(26):
    t = ""
    print('rot{}:-------------------------------'.format(j))
    for s in S:
        if s.isalpha():
            if s.isupper():
                r = ord('A')
            else:
                r = ord('a')
            s = ord(s) - r
            s = chr((s + j) % 26 + r)

        t += s
    print(t)
