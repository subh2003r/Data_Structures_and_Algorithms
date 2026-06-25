from functools import lru_cache

def memoized_approach(str1, str2):
    """
    Here lru_cache stores the intermediate results and is similar to how we do in memoization approach 
    Here, time complexity = No of states * Work done per state 
    Work done per state = Length of the string while concatenating (worst case, it would be m+ n)
    Time complexity = O(m*n*(m+n))
    Space complexity = Total size of memoized table, each cell stores a max length string of m+n + recursion depth 
    recursion depth = O(max(m,n))
    Table size = O(m*n*(m+n))
    Final space complexity = O(m*n*(m+n) + m*n)
    """

    @lru_cache(None)
    def solve(i, j):
        if i == len(str1):
            return str2[j:]
        if j == len(str2):
            return str1[i:]

        if str1[i] == str2[j]:
            return str1[i] + solve(i+1, j+1)
        else:
            left = str1[i] + solve(i+1, j)
            right = str2[j] + solve(i, j+1)

            if len(left) <= len(right):
                return left 
            else:
                return right
    
    return solve(0,0)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m, n = len(str1), len(str2)

        # LCS DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        # Build SCS
        i, j = m, n
        ans = []

        while i > 0 and j > 0:

            if str1[i - 1] == str2[j - 1]:

                ans.append(str1[i - 1])
                i -= 1
                j -= 1

            elif dp[i - 1][j] > dp[i][j - 1]:

                ans.append(str1[i - 1])
                i -= 1

            else:

                ans.append(str2[j - 1])
                j -= 1

        while i > 0:
            ans.append(str1[i - 1])
            i -= 1

        while j > 0:
            ans.append(str2[j - 1])
            j -= 1

        return "".join(reversed(ans))