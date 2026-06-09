class Solution:
    def bruteApproach(self, nums):
        
        # brute force approach 
        """
        -- Storing subsets of len 15, lets suppose each python integer is 4 bytes, so for 15 integers, total bytes = 60 bytes, and overall subset stores of len 15 = 30C15, and total memory store = 30C15 * 60 bytes ~ 9 GB which causes Memory limit exceeded.
        """
        
        n = len(nums)
        total_sum = sum(nums)
        split = n // 2

        storeA_sub = []

        def findSubset(index, curr_sub):
            if index >= n:
                return 

            if len(curr_sub) == split:
                storeA_sub.append(curr_sub[:])
                return
            
            # take the current element 
            curr_sub.append(nums[index])
            findSubset(index+1, curr_sub)
            # skip the current element
            curr_sub.pop()
            findSubset(index+1, curr_sub)

        # invoke the function
        findSubset(0, [])

        diff = float("inf")
        for subset in storeA_sub:
            sumA = sum(subset)
            diff = min(diff, abs(total_sum - 2*sumA))
        
        return diff

    def minimumDifference(self, nums: List[int]) -> int:
        # optimised approach 
        """
        1. Split into two halves 
        2. Generate all subsets sum of each half 
        3. Group sums by subset size 
        4. Sort right halves group
        5. For every left sum, determines 
            - how many elements are still needed
            - binary search the matching right group for the closest sum 
        6. Update answer
        """
        total = sum(nums)
        n = len(nums) // 2
        left = nums[:n]
        right = nums[n:]

        left_sum = [[] for _ in range(n+1)]
        right_sum = [[] for _ in range(n+1)]
        
        def binary_search(arr, low, high, target):
            
            while low <= high:
                mid = (low+high) // 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
                
            return low

        def generate_func(arr, idx, count, curr_sum, store):
            if idx == len(arr):
                store[count].append(curr_sum)
                return
            
            # pick the index 
            generate_func(arr, idx+1, count+1, curr_sum+arr[idx], store)
            # skip the index 
            generate_func(arr, idx+1, count, curr_sum, store)
        
        generate_func(left, 0,0, 0, left_sum)
        generate_func(right, 0,0, 0, right_sum)

        for k in range(n+1):
            right_sum[k].sort()

        res = float("inf")

        for k in range(n+1):
            right_bucket = right_sum[n-k]
            
            for x in left_sum[k]:
                target = total/2 - x
                pos = binary_search(right_bucket, 0, len(right_bucket)-1, target)

                # check candidate at pos
                if pos < len(right_bucket):
                    choosen_sum = x + right_bucket[pos]
                    res = min(res, abs(total - 2*choosen_sum))
                # check candidate at pos-1
                if pos > 0:
                    choosen_sum = x + right_bucket[pos-1]
                    res = min(res, abs(total - 2*choosen_sum))
        
        return res