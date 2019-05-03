"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
"""

"""
def rotateImage(a):
    def clkw_r(i, j, n):
        return j, n-i-1

    n = len(a)
    r = n // 2
    for d in range(r):
        ib, jb = d, d
        for x in range(d,n-d-1):
            i, j = ib, jb+x
            save = a[i][j]
            for _ in range(4):
                in_, jn = clkw_r(i, j, n)
                tmp = a[in_][jn]
                a[in_][jn] = save
                save = tmp # new will be current next
                i, j = in_, jn"""

def rotateImage(a):
    n = len(a)
    for i in range(n//2):
        for j in range(i, n-i-1):
            s = a[i][j]
            a[i][j] = a[n- 1 - j][i]
            a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j]
            a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i]
            a[j][n - 1 - i] = s
    return a

