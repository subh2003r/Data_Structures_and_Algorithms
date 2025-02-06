#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        arr.sort()
        
        largest = arr[n-1]
        i = n-2
        while i >= 0:
            if arr[i] != largest:
                return arr[i]
            i -= 1
        
        return -1

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends