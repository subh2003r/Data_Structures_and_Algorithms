class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        Time complexity: O(n2 * L) -- as unique states is n^2 
        One observation -- initally i used memoization using dp = {}, but that caused memory limit exceeded because a dictionary has a lot of overhead associated ranging from storing the tuple(idx, prev), hash, integer object .. which causes the memory to shoot up .. but if we use normal 2D array for two states , then the memory consumption will be less hence preventing Memory Limit exceed (MLE)
        """
        n = len(words)
        # sort the words based on the length
        words.sort(key=len)
        dp = [[-1]*(n+1) for _ in range(n)]
        
        def checkPred(w1, w2):
            i, j = 0, 0
            n, m = len(w1), len(w2)
            if abs(n-m) != 1:
                return False
            
            while i < n and j < m:
                if w1[i] == w2[j]:
                    i += 1
                j += 1
            
            return i == n

        def solve(idx, prev):
            if idx >= n:
                return 0
            
            if dp[idx][prev+1] != -1:
                return dp[idx][prev+1]

            take = 0
            if prev == -1 or checkPred(words[prev], words[idx]):
                take = 1 + solve(idx+1, idx)
            
            notTake = solve(idx+1, prev)
            dp[idx][prev+1] = max(take, notTake)
            
            return dp[idx][prev+1]
        
        return solve(0, -1)


