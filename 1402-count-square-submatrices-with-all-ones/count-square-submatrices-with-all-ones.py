from functools import lru_cache

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        @lru_cache(None)
        def brute(i, j):
            if i < 0 or j < 0:
                return 0
            
            if matrix[i][j] == 0:
                return 0

            if i == 0 or j == 0:
                return 1
            
            left = brute(i, j-1)
            top = brute(i-1, j)
            diag = brute(i-1, j-1)

            return 1 + min(left, top, diag)
        
        res = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    res += brute(i, j)

        return res
        

            