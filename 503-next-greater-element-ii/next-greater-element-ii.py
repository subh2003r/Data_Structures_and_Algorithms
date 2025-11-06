class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1]*n
        st = []

        for index in range(2*n-1, -1, -1):
            while st and st[-1] <= nums[index % n]:
                st.pop()
            
            if index < n:
                nge[index] = st[-1] if st else -1
            
            st.append(nums[index % n])
        
        return nge


    