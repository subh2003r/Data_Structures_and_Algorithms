class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        One way is to generate subsequences using memoized approach and then comparing with t and updating the count sequence
        and another approach is that instead of building the subsequence, we track how much of 't' has been matched with 's'
        """

        m, n = len(s), len(t)
        dp = {}
        
        def solve(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            
            if (i, j) in dp:
                return dp[(i,j)]
            
            if s[i] == t[j]:
                take = solve(i-1, j-1)
                not_take = solve(i-1, j)

                dp[(i, j)] = take + not_take
            else:
                dp[(i, j)] = solve(i-1, j)
            
            return dp[(i, j)]
        
        return solve(m-1, n-1)