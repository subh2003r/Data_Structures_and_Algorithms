#User function Template for python3
class Solution:
    '''
    Why Can't We Add a List to a Set?
    In Python, lists are mutable, meaning they can change after creation. However, sets only store immutable (hashable) elements.

    A list is not hashable, so when you try to add a list to a set, you get an error:
    s = set()
    s.add([1, 2, 3])  # ❌ TypeError: unhashable type: 'list'
    What Does "Unhashable" Mean?
    Sets use a hash table to store unique elements efficiently.
    A hash value is a unique identifier for an object.
    Mutable objects (like lists) can change, meaning their hash value would also change, making them unsuitable for a set.
    Immutable objects (like tuples, strings, and numbers) are hashable because their value remains constant.
    '''
        
    def recur(self,index,arr,target,memo):
        if index >= len(arr):
            return 1 if target == 0 else 0
        
        if (index,target) in memo:
            return memo[(index,target)]
        
        # subSeq.append(arr[index])
        left = self.recur(index+1,arr,target-arr[index],memo)
        # subSeq.pop()
        right = self.recur(index+1,arr,target,memo)
        
        memo[(index,target)] = left+right
        
        return memo[(index,target)]
    
	def perfectSum(self, arr, target):
		# code here
		return self.recur(0,arr,target,{})
		
		
        
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array input
        target = int(input().strip())  # Read the target sum
        ob = Solution()  # Create the Solution object
        print(ob.perfectSum(arr, target))  # Call perfectSum with 2 arguments
        tc -= 1  # Decrease test case count
        print("~")
# } Driver Code Ends