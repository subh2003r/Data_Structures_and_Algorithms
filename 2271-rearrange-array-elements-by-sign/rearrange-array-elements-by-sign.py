class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        neg, pos = 1, 0

        for value in nums:
            if value >= 0:
                res[pos] = value
                pos += 2
            else:
                res[neg] = value
                neg += 2
        
        return res

    