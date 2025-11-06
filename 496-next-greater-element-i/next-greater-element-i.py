class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        next_great = {}
        final_res = []

        for value in nums2:
            while st and st[-1] < value:
                next_great[st.pop()] = value

            st.append(value)

        for value in nums1:
            final_res.append(next_great[value] if value in next_great else -1)
    
        return final_res
        