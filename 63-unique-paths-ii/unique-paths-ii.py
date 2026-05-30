class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        BFS cannot be used to solve this problem, BFS answers: "What is the minimum number of steps to reach the destination ?"
        DFS answers: "What are the possible ways to reach the destination?"
        """
        m,n = len(obstacleGrid), len(obstacleGrid[0]) 
        dp = [[-1]*n for _ in range(m)]
        dp[0][0] = 1
        
        def recur(i,j):
            if i < 0 or j < 0:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            up = recur(i-1, j)
            left = recur(i, j-1)

            dp[i][j] = up+left
            return dp[i][j]            
        
        return recur(m-1, n-1)