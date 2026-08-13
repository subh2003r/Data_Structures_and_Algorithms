class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Every element we can:
        Either start a new subarray from 'x' or,
        continue the previous subarray, so 'prev_sum + x'
        """

        # one optimal approach
        total,max_sum = 0,float("-inf")
        n = len(nums)
        
        for i in range(n):
            total += nums[i]
            max_sum = max(max_sum,total)
            total = total if total > 0 else 0

        return max_sum

