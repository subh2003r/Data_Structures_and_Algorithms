# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        '''
        two approach to solve this problem 
        1) positive elements is present
        2) positive and negative elements are present
        '''
        max_consec = 0
        store = dict()
        cum_sum = 0
        
        for i in range(len(arr)):
            cum_sum += arr[i]
            if cum_sum == k:
                max_consec = max(max_consec,i+1)
            rem = cum_sum - k
            if rem in store:
                max_consec = max(max_consec,i-store[rem])
            
            if cum_sum not in store:
                store[cum_sum] = i
        
        return max_consec


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends