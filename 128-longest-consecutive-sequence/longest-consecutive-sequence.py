class Solution:
    '''
    def linear_search(self, nums, value):
        for x in nums:
            if value == x:
                return True
        return False
    '''

    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        # brute force approach
        n = len(nums)

        max_len = float("-inf")
        for i in range(0,n):
            cnt = 1
            value = nums[i]
            while (self.linear_search(nums, value+1)):
                cnt += 1
                value = value+1
            
            max_len = max(max_len, cnt)

        return max_len
        '''

        '''
        # sorting approach (better approach)

        if not nums:
            return 0

        nums.sort()
        n = len(nums)

        prev = nums[0]
        max_len = 1
        cnt = 1

        for curr in nums[1:]:
            if curr-1 == prev:
                cnt += 1
            elif curr == prev:
                continue
            else:
                max_len = max(max_len, cnt)
                cnt = 1
            
            prev = curr
        
        max_len = max(max_len, cnt)

        return max_len
        '''


        store = set(nums)
        res = 0

        for num in store:
            if num-1 not in store:
                curr = num
                length = 1

                while curr+1 in store:
                    length += 1
                    curr += 1
                
                res = max(res, length)
            
        return res
                