class Solution:
    def __init__(self):
        self.store = []

    def recur(self,index,nums,subSeq):
        self.store.append(subSeq[:])

        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subSeq.append(nums[i])
            self.recur(i+1,nums,subSeq)
            subSeq.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.recur(0,nums,[])
        return self.store