class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,major_ele = 0,0
        n = len(nums)
        for i in range(n):
            if count == 0:
                major_ele = nums[i]
            if major_ele != nums[i]:
                count -= 1
            else:
                count += 1
        return major_ele