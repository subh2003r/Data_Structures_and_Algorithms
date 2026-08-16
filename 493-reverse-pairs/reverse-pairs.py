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
        """
        # Brute force approach - O(n^2)
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > 2*nums[j]:
                    count += 1

        return count
        """
        """
        Optimal appraoch using merge sort
        Intuition:-
        Merge sort splits the array into left and right. Any reverse pair is either completely inside the left, completely inside the right, or crosses from left to right. Recursion handles the first two. Because the two halves are sorted, two pointers can count all cross pairs in O(n). Then we merge the halves so they stay sorted for the next level.
        """

        # start, end = 0, len(nums)-1
        # # creating a copy of the original list 
        # nums_copy = nums[:]

        # return self.mergeSort(nums, start, end)

        def merge(start, mid, end):           
            i, j = start, mid+1
            temp = []
            rev = 0

            idxL = start # key optimization -- stored outside the loop
            # find the reverse pairs with sorted left and right halves
            for idxR in range(mid+1, end+1):
                while idxL <= mid and nums[idxL] <= 2*nums[idxR]:
                    idxL += 1
                
                rev += mid-idxL+1

            # Merging the sorted halves -- 
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            for i in range(len(temp)):
                nums[start+i] = temp[i]
            
            return rev

        def mergeSort(start, end):
            rev = 0
            if start >= end:
                return 0
            mid = (start + end) // 2

            rev += mergeSort(start, mid)
            rev += mergeSort(mid+1, end)

            rev += merge(start, mid, end)
            return rev
        
        start, end = 0, len(nums)-1
        return mergeSort(start, end)






