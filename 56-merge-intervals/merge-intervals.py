class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        # merged = []
        
        # currStart, currEnd = intervals[0]
        # # scan the intervals
        # for start, end in intervals[1:]:
        #     if start <= currEnd:
        #         currStart = min(currStart, start)
        #         currEnd = max(currEnd, end)
        #     else:
        #         merged.append([currStart, currEnd])
        #         currStart = start
        #         currEnd = end

        # # append the last interval
        # merged.append([currStart, currEnd])

        # return merged

        intervals.sort(key = lambda x: x[0])
        currStart, currEnd = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if start <= currEnd:
                currStart = min(currStart, start)
                currEnd = max(currEnd, end)
            else:
                res.append([currStart, currEnd])
                currStart = start
                currEnd= end
        
        res.append([currStart, currEnd])
        return res
