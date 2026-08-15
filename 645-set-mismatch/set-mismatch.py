class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeat, miss = -1, -1
        store = {i: 0 for i in range(1, n+1)}

        for value in nums:
            store[value] += 1
            if store[value] > 1:
                repeat = value

        for key, count in store.items():
            if count == 0:
                miss = key
                break

        return [repeat, miss]

        

        

        