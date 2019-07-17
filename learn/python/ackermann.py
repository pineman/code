import sys

def ackermann(m, n):
    if m < 0 or n < 0:
        sys.exit()

    #print(f'ackermann called with {m, n}')
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

sys.setrecursionlimit(9999999)
for i in range(6):
    for j in range(6):
        print(f'ackermann({i}, {j}) is {ackermann(i, j)}')
