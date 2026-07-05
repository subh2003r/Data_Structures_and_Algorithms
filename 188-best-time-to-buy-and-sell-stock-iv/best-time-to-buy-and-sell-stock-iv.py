class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]

        def stocks(i, buy, cap):
            if i == n:
                return 0
            if cap == 0:
                return 0
            
            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]
            
            if buy:
                take = -prices[i] + stocks(i+1, 0, cap)
                skip = stocks(i+1, 1, cap)
                dp[i][buy][cap] = max(take, skip)
            else:
                take = prices[i] + stocks(i+1, 1, cap-1)
                skip = stocks(i+1, 0, cap)
                dp[i][buy][cap] = max(take, skip)
            
            return dp[i][buy][cap]
            
        return stocks(0, 1, k)
        