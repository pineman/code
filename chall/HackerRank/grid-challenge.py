#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    n = len(grid[0])
    # The problem statement effing lies and the matrix can be non-square.
    cols = ['']*n
    for r, row in enumerate(grid):
        grid[r] = "".join(sorted(row))
        for i in range(n):
            cols[i] += grid[r][i]
    print(grid)
    for col in cols:
        for i in range(n-1):
            if col[i] > col[i+1]:
                print(col[i], col[i+1])
                print('NO')
                return 'NO'
    print('YES')
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
