from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        # create dist 2D array with n cols and m rows 
        dist = [[float("inf")]*n for _ in range(m)]
        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        dist[0][0] = 0

        dq = deque([(0,0,0)]) # push row, col, effort

        while dq:
            row, col, stored_effort = dq.popleft()
            prev_effort = dist[row][col]
            if stored_effort > prev_effort:
                continue

            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_effort = abs(heights[nr][nc] - heights[row][col])
                    curr_effort = max(prev_effort, new_effort)
                    if curr_effort < dist[nr][nc]:
                        dist[nr][nc] = curr_effort
                        dq.append((nr,nc, curr_effort))

        return dist[m-1][n-1]
            