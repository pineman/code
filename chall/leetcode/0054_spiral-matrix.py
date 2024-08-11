class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = []
        while True:
            m = len(matrix)
            if m == 0:
                break
            n = len(matrix[0])
            if n == 0:
                break
            if m == 1:
                r += matrix[0]
                break
            if n == 1:
                for row in matrix:
                    r += row
                break
            for i in range(0, n):
                r.append(matrix[0][i])
            for i in range(1, m):
                r.append(matrix[i][n-1])
            for i in range(n-2, 0, -1):
                r.append(matrix[m-1][i])
            for i in range(m-1, 0, -1):
                r.append(matrix[i][0])
            for i, row in enumerate(matrix):
                matrix[i] = row[1:len(row)-1]
            matrix = matrix[1:len(matrix)-1]
        return r
