class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_num = k

        for value in arr:
            if value <= missing_num:
                missing_num += 1
        
        return missing_num