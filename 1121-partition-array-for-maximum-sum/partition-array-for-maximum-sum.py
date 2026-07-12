class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            curr_max = 0
            ans = 0
            for j in range(i, min(i+k, n)):
                curr_max = max(curr_max, arr[j])
                leng = j-i+1

                ans = max(ans, curr_max*leng + dp[j+1])
            
            dp[i] = ans
        
        return dp[0]