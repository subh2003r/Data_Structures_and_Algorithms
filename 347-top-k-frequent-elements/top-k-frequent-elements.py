from collections import Counter
import heapq
"""
Using minheap
# Space complexity: O(k)
# Time complexity: O(n) + O(nlogk)
"""

"""
Using bucket sort
# Space complexity: O(n)
# Time complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort
        result = []
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key, count in freq.items():
            bucket[count].append(key)

        for i in range(len(bucket)-1, -1, -1):
            for key in bucket[i]:
                result.append(key)
                if len(result) == k:
                    return result
        
        return result

        """
        # minheap
        freq = Counter(nums)
        heap = []
        
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [key for _, key in heap] 
        """
        