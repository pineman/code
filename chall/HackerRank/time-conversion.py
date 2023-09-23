#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm = s[-2:]
    s = s[:-2]
    hour = s[:2]
    if ampm == 'PM' and hour != "12":
        return str(int(s[:2])+12) + s[2:]
    if ampm == 'AM' and hour == "12":
            return "00" + s[2:]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()