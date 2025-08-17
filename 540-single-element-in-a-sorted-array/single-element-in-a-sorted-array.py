class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # naive approach 
        n = len(nums)

        if n==1:
            return nums[0]

        for i in range(n):
            if i==0:
                if nums[i] != nums[i+1]:
                    return nums[i]
            elif i==n-1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            else:
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]

        