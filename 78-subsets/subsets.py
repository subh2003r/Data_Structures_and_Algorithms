# 1) first approach -> solve using power set 
# check whether ith bit is set, if it is set then include its corresponding element else not 

# 2) second approach -> solve using recursion

class Solution:
    def __init__(self):
        self.store = []

    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 2**n
        store = []

        for i in range(m): # run till 2**n-1
            subSeq = []
            for j in range(n):  # run through the every bits
                # checking whether the ith bit is set or not
                if (i & (1 << j)):
                    subSeq.append(nums[j])
            store.append(subSeq)

        return store
        '''

    def recur(self,nums,index,subSeq):
        '''
        Why does subSeq[:] fix the issue?
    subSeq[:] creates a shallow copy of the list.
    The copy is stored in self.store, so future modifications to subSeq do not affect       previously stored subsets.

        '''
        if index == len(nums):
            self.store.append(subSeq[:]) # append a copy of subSeq
            return
        
        # pick the element
        subSeq.append(nums[index])
        self.recur(nums,index+1,subSeq)
        subSeq.pop() # backtrack
        # do not pick the element
        self.recur(nums,index+1,subSeq)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.recur(nums,0,[])
        return self.store