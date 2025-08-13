class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)

        # sorting the intervals
        intervals.sort()

        # brute force approach 
        for i in range(0,n):
            start, end = intervals[i][0], intervals[i][1]  

            if res and res[-1][1] >= end:
                continue

            for j in range(i+1,n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break

            res.append([start,end])

        return res