class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        # Brute force approach

        n = len(nums)
        store = set()

        for i in range(0,n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+num[j]+nums[k] == 0:
                        store.add(tuple(sorted([nums[i],nums[j],nums[k]])))

        return [list(s) for s in store]


        # Better approach 
        res = set()

        for i in range(0, n):
            store = set()
            for j in range(i+1, n):
                target = -(nums[i]+nums[j])

                if target in store:
                    res.add(tuple(sorted([nums[i],nums[j], target])))

                store.add(nums[j])

        return [list(t) for t in res]
        '''

        # best approach 

        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i+1
            end = n-1

            while start < end:
                target = nums[i] + nums[start] + nums[end]
                if target == 0:
                    res.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif target < 0:
                    start += 1
                else:
                    end -= 1
        
        return res