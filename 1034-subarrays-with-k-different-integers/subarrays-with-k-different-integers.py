class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(goal):
            if goal < 0:
                return 0
            
            left, right = 0, 0
            n = len(nums)
            count = 0
            
            store = {}
            while right < n:
                store[nums[right]] = store.get(nums[right], 0)+1

                while len(store) > goal:
                    store[nums[left]] = store.get(nums[left])-1
                    if store[nums[left]] == 0:
                        store.pop(nums[left])
                    left += 1

                count += right-left+1
                
                right += 1
            
            return count

        return atmost(k) - atmost(k-1)
