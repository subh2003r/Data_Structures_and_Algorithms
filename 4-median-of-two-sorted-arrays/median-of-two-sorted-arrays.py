import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # start iteration from the smaller length array
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, n
        total = n+m 
        left = math.ceil(total/2)

        while low <= high:
            mid = (low + high)//2
            l1 = nums1[mid-1] if mid-1 >= 0 else float("-inf")
            l2 = nums2[left-mid-1] if left-mid-1 >= 0 else float("-inf")
            r1 = nums1[mid] if mid < n else float("inf")
            r2 = nums2[left-mid] if left-mid < m else float("inf")

            if l1 <= r2 and l2 <= r1:
                if total%2:
                    return max(l1,l2)
                else:
                    return (max(l1,l2) + min(r1,r2))/2
            elif l1 > r2:
                high = mid-1
            else:
                low = mid+1
        
        return -1
