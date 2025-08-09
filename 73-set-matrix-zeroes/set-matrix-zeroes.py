class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])

        '''
        row, col = [0]*m, [0]*n
        # brute force approach

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

        '''

        col0 = 1 # to keep track of col0 as it was overallaped i.e handling edge cases

        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

    # Step 2: Fill zeros in reverse order to protect markers
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

