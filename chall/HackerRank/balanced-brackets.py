#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def isOpen(c):
    return c == '{' or c == '[' or c == '('

def closes(c, o):
    if c == ')':
        return o == '('
    elif c == ']':
        return o == '['
    elif c == '}':
        return o == '{'
    return False


def isBalanced(s):
    # Write your code here
    st = []
    for c in s:
        if isOpen(c):
            st.append(c)
            continue
        if len(st) == 0:
            return 'NO'
        if not closes(c, st[-1]):
            return 'NO'
        else:
            st.pop()
    if len(st) > 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
