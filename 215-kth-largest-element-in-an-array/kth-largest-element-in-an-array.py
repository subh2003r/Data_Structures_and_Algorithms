"""
1. using heapq (Time complx: O(n*logK), where K is 'k') 
"""
import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        store = []

        for i in range(len(nums)):
            hp.heappush(store, nums[i])
            if len(store) > k:
                hp.heappop(store)

        return hp.heappop(store)

        
