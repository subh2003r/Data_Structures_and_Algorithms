class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """ 
        1. Highly brute force approach:- Generate all possible subsets from the given list and for each subsets, check for each pair if they are divisible either way .. O(2^n * n^2)

        2. if we sort the array, then instead of checking for all the pairs of divisibility, we can check with the last stored element with the current element, -- O(2^n) -- code mentioned in bruteForce() function

        3. Memoized brute force approach -- Time complex: O(n*(n+1)) = O(n^2)
        4. Optimal approach -- single dimension dp state, traceback the elements using parent 
        """

        n = len(nums)
        nums.sort()


        def bruteForce(idx, prev):
            if idx >= n:
                return []
            
            take = []
            if prev == -1 or nums[idx] % nums[prev] == 0:
                take = [nums[idx]] + bruteForce(idx+1, idx)
            
            notTake = bruteForce(idx+1, prev)

            if len(take) > len(notTake):
                return take
            
            return notTake
        
        # dp dictionary 
        dp = {}

        def memoizebruteForce(idx, prev):
            if idx >= n:
                return []
            
            if (idx, prev) in dp:
                return dp[(idx, prev)]

            take = []
            if prev == -1 or nums[idx] % nums[prev] == 0:
                take = [nums[idx]] + bruteForce(idx+1, idx)
            
            notTake = bruteForce(idx+1, prev)

            if len(take) > len(notTake):
                dp[(idx, prev)] = take
            else:
                dp[(idx, prev)] = notTake

            return dp[(idx, prev)]
        
        # return memoizebruteForce(0, -1)

        def optimalApproach():
            # sort the array -- already done globally 
            # find max subset length (common to Lis)
            dp = [1]*n     # each element independently have an length 1 
            parent = [-1]*n
            maxLen = 0
            maxIndex = 0
            res = []

            for i in range(1, n):
                for j in range(i):
                    if nums[i] % nums[j] == 0:
                        if dp[j]+1 > dp[i]:
                            dp[i] = 1 + dp[j]
                            parent[i] = j

                if maxLen < dp[i]:
                    maxLen = dp[i]
                    maxIndex = i
            
            while maxIndex != -1:
                res.append(nums[maxIndex])
                maxIndex = parent[maxIndex]
            
            res.reverse()
            return res
        
        return optimalApproach()


