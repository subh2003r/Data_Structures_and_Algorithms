class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Obs:
        - At least one num
        - k >= 1
        - num >= 1
        
        Approaches:
        1) Brute force all possible pairs ~ O(n^2)
        2) 2 pointers somehow???
        3) Could count all occurences of nums O(n). Then for each num(check complement if it exists we can deduct a pair). Repeat for all nums O(n). Should be overall O(n)!!!!

        Time: O(2n) = O(n)
        Space: O(n)
        """
        nums_to_count = {} # {num: count}

        for num in nums:
            if num in nums_to_count:
                nums_to_count[num] += 1
            else:
                nums_to_count[num] = 1
        
        pairs = 0

        for num in nums_to_count:
            # Edge Case: If num >= k then it can't sum to it with another num
            if num >= k:
                continue
            
            comp = abs(num - k)

            # We still have potential matches for this num
            while nums_to_count[num]: 
                # Edge Cases: 
                # - The complement is itself so we need 2 or more
                if comp == num and nums_to_count[num] < 2:
                    break

                # If the complement exists and is non-zero for matching
                if comp in nums_to_count and nums_to_count[comp]: 
                    nums_to_count[num] -= 1
                    nums_to_count[comp] -= 1
                    pairs += 1
                else:
                    break


        return pairs

        