#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    p1, p2, p3 = 1, 2, 3
    t = 0
    for i, v in enumerate(q):
        if v == p1:
            p1 = p2
            p2 = p3
            p3 += 1
        elif v == p2:
            t += 1
            p2 = p3
            p3 += 1
        elif v == p3:
            t += 2
            p3 += 1
        else:
            print('Too chaotic')
            return
    print(t)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
