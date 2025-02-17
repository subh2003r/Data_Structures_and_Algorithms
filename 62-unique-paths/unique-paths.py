class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP array initialized with 0
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and first column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the value in the bottom-right corner
        return dp[m-1][n-1]