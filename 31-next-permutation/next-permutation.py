class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Identify the breakpoint, where the element from the last is increasing, find the place where the element suddenly decreases(this element is the breakpoint)
        Then swap the element with the other element on the right side which is near to greater than the breakpoint element
        After swapping the elements, reverse the element on the right side of the breakpoint element (no need to sort them, only reverse them as they will be in reverse sorted form)
        """
        
        """
        Similar question is Previous smaller permutation
        """
        
        n = len(nums)

        breakpoint_index = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                breakpoint_index = i
                break

        if breakpoint_index != -1:
            great_ele = breakpoint_index + 1

            for i in range(breakpoint_index+1, n, 1):
                if (nums[i] > nums[breakpoint_index]) and (nums[i] <= nums[great_ele]):
                    great_ele = i
            
            nums[great_ele], nums[breakpoint_index] = nums[breakpoint_index], nums[great_ele]

        start = breakpoint_index + 1
        end = n-1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
        
        
            