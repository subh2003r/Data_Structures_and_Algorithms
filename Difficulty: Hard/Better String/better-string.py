#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countDistinctSubseq(self,s):
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        
        last_seen = {}
        
        for i in range(1,n+1):
            char = s[i-1]
            dp[i] = 2*dp[i-1]
            
            if char in last_seen:
                dp[i] -= dp[last_seen[char]-1]
            
            last_seen[char] = i
            
        return dp[n]
        
    def betterString(self, str1, str2):
        # Code here
        count1 = self.countDistinctSubseq(str1)
        count2 = self.countDistinctSubseq(str2)

        return str1 if count1 >= count2 else str2

        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
        print("~")
# } Driver Code Ends