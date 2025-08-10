import sys
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        n = len(nums)
        res = []

        count1,count2 = 0,0
        ele1,ele2 = float('-inf'),float(-inf)

        for i in range(n):
            if ((count1 == 0) and (nums[i] != ele2)):
                count1 = 1
                ele1 = nums[i] 
            elif ((count2 == 0) and (nums[i] != ele1)):
                count2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        # the two elements left after performing the boyers voting algo are the frequent candidates 

        # performing another check to make sure that these elements are >= n//3+1
        count1,count2 = 0,0
        for i in range(n):
            if nums[i] == ele1:
                count1 += 1
            if nums[i] == ele2:
                count2 += 1
        
        mini = n//3 + 1
        if count1 >= mini:
            res.append(ele1)
        if count2 >= mini:
            res.append(ele2)
        return res
        '''

        ele1, ele2 = float("-inf"), float("-inf")
        cnt1, cnt2 = 0, 0

        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != ele2:
                cnt1,ele1 = 1, nums[i]
            elif cnt2 == 0 and nums[i] != ele1:
                cnt2,ele2 = 1, nums[i]
            elif nums[i] == ele1:
                cnt1 += 1
            elif nums[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0,0

        for value in nums:
            if ele1 == value:
                cnt1 += 1
            elif ele2 == value:
                cnt2 += 1
        
        mini = len(nums)//3 + 1
        res = []

        if cnt1 >= mini:
            res.append(ele1)
        if cnt2 >= mini:
            res.append(ele2)

        return res
        