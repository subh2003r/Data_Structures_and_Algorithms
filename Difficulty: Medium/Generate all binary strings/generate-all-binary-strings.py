#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def recur(self,store,n,newStr):
        if len(newStr) == n:
            store.append(newStr)
            return
        
        self.recur(store,n,newStr+'0')
        if len(newStr) >= 1 and newStr[-1] == '0' or len(newStr) == 0:
            self.recur(store,n,newStr+'1')
        
    def generateBinaryStrings(self, n):
        # Code here
        store = []
        self.recur(store,n,"")
        
        return store
        
        

#{ 
 # Driver Code Starts.
from sys import stdout
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        res = ob.generateBinaryStrings(N)
        for binaryString in res:
            print(binaryString, end = ' ')
        print()
        print("~")
# } Driver Code Ends