#User function Template for python3
class Solution:
    def __init__(self):
        self.store = []
        
    def recur(self,arr,index,value):
        if index == len(arr):
            self.store.append(value)
            return
        
        self.recur(arr,index+1,value)
        self.recur(arr,index+1,value+arr[index])
        
	def subsetSums(self, arr):
		# code here
        self.recur(arr,0,0)
        return self.store

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        arr = [int(x)
               for x in input().split()]  # Reading array for the test case
        ob = Solution()
        ans = ob.subsetSums(arr)  # Getting the subset sums
        ans.sort()  # Sorting the result

        # Printing the subset sums in space-separated format
        for x in ans:
            print(x, end=" ")
        print("")  # Ensuring new line after each test case

# } Driver Code Ends