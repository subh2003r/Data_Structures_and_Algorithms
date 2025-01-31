# 1) first approach -> solve using power set 
# check whether ith bit is set, if it is set then include its corresponding element else not 

class Solution:
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