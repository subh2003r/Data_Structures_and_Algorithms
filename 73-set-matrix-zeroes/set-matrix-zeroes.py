class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])

        row, col = [0]*m, [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # marking the corresponding row and col to 1 for keeping track of zeros
                    row[i], col[j] = 1, 1
        

        # marking the corresponding cells as zeros 
        for i in range(m):
            for j in range(n):
                # if either of them is 1
                if row[i] or col[j]:
                    matrix[i][j] = 0

        