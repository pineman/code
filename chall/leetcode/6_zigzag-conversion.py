class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = [[]]*numRows
        chunk_size = 0
        if numRows > 2:
            chunk_size = numRows*2 - 2
        else:
            chunk_size = numRows
        for i in range(0,len(s),chunk_size):
            try:
                for j in range(numRows):
                    m[j] = m[j] + [s[i+j]]
                for j in range(numRows, chunk_size):
                    diag_row = chunk_size-j
                    m[diag_row] = m[diag_row] + [s[i+j]]
            except IndexError:
                break
        r = ''
        for l in m:
            for c in l:
                r += c
        return r
