class Solution:
    def search_first(self, nums, target):
        low, high = 0, len(nums)-1
        first = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                first = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        
        return first 
    
    def search_last(self, nums, target):
        low, high = 0, len(nums)-1
        last = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                last = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1st approach -> find lower and upper bound, handle cases where target is not present in the list 
        # other approach
        first = self.search_first(nums, target)
        if first == -1:
            return [-1,-1]
        last = self.search_last(nums, target)

        return [first, last]
