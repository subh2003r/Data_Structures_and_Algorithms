class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Time complexity for brute force:- exponential and space complexity is O(k)
        Time complexity for DP memoized:- O(n^2) -- n^2 unique states and space complexity: O(n^2)
        """
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[-1]*m for _ in range(m)]
            
        def solve(i, j):
            if abs(i-j) <= 1:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            res = float("inf")
            for k in range(i+1, j):
                cost = (
                    solve(i,k) + solve(k,j) + cuts[j]-cuts[i]
                )
                res = min(res, cost)
            
            dp[i][j] = res
            return dp[i][j]
        
        return solve(0, m-1)