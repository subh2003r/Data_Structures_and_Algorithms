class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find previous and next smaller elements for each bar
        and calculate maximum area 
        """
        n = len(heights)
        st = []
        max_area = 0

        for index in range(n):
            while st and heights[st[-1]] >= heights[index]:
                pop_index = st.pop()
                nse = index    # next smaller index
                pse = st[-1] if st else -1     # previous smaller index

                max_area = max(max_area, (nse-pse-1)*heights[pop_index])

            st.append(index)

        while st:
            pop_index = st.pop()
            nse = n
            pse = st[-1] if st else -1

            max_area = max(max_area, (nse-pse-1)*heights[pop_index])

        return max_area

        return max_area