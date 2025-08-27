import math
class Solution:
    def check_hours(self,bananas, hour, piles):
        overall_hrs = 0
        # total hours taken for koko to eat given bananas per hour
        for pile in piles:
            overall_hrs += math.ceil(pile/bananas)

        return 0 if overall_hrs <= hour else 1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = float("-inf")
        # per hour, koko can eat the max bananas present in the pile
        for banana in piles:
            max_bananas = max(max_bananas, banana)
        
        low, high = 1, max_bananas

        while low <= high:
            mid = (low+high)//2
            res = self.check_hours(mid,h,piles)
            if res == 0:
                high = mid-1
            else:
                low = mid+1

        return low

