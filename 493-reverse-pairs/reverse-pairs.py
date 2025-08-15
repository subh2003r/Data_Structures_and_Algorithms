class Solution:
    def merge(self, nums, start, mid, end):
        temp = []
        left, right = start, mid+1
        reverse = 0

        for i in range(left, right):
            while right <= end and nums[i] > 2*nums[right]:
                right += 1
            reverse += right-(mid+1)

        left, right = start, mid+1

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
            
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= end:
            temp.append(nums[right])
            right += 1

        for i in range(len(temp)):
            nums[start+i] = temp[i]

        return reverse

    def mergeSort(self, nums, start, end):
        reverse = 0   

        if start >= end:
            return 0
        
        mid = (start + end)//2

        reverse += self.mergeSort(nums, start, mid)
        reverse += self.mergeSort(nums, mid+1, end)

        reverse += self.merge(nums, start, mid, end)

        return reverse


    def reversePairs(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        # creating a copy of the original list 
        nums_copy = nums[:]

        return self.mergeSort(nums, start, end)

