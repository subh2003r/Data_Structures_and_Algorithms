from functools import lru_cache

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def tabulation():
            dp = [[0]*m for _ in range(n)]
            res = 0

            for i in range(n):
                for j in range(m):
                    if matrix[i][j] == 1:
                        if i == 0 or j == 0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = 1 + min(
                                dp[i-1][j],
                                dp[i][j-1],
                                dp[i-1][j-1]
                            )
                        
                        res += dp[i][j]
                
            return res           

        return tabulation()

        @lru_cache(None)
        def memo(i, j):
            if i < 0 or j < 0:
                return 0
            
            if matrix[i][j] == 0:
                return 0

            if i == 0 or j == 0:
                return 1
            
            left = memo(i, j-1)
            top = memo(i-1, j)
            diag = memo(i-1, j-1)

            return 1 + min(left, top, diag)
        
        res = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    res += memo(i, j)

        return res
        

            