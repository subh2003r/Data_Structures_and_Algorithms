class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        dp(left) and dp(right) are independent subproblems—they don't execute one after the other; they only guarantee that all balloons in their respective intervals are burst before k.
Choosing k as the last balloon means that when k is finally burst, every balloon in both its left and right intervals has already disappeared, making its neighbours fixed (i-1 and j+1).
        """
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[-1]*n for _ in range(n)]

        def burst(i, j):
            if i > j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
                
            res = 0
            for k in range(i, j+1):
                coins = (
                    nums[i-1]*nums[k]*nums[j+1] +
                    burst(i, k-1) +
                    burst(k+1, j)
                )

                res = max(res, coins)
            
            dp[i][j] = res
            return dp[i][j]
         
        return burst(1, len(nums)-2)


