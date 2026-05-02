from collections import deque
import heapq as hq 

class Solution:
    def simple_bfs(self, heights):
        """
        Normal BFS approach 
        Only issue is the node processing order --> BFS processes in FIFO order 
        Nodes can be visited multiple times .. thus increasing time complexity
        """
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
            
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Using dijkstra algo, here it will gurantee minimum effort across path to reach the destination. Because at a time, dijkstra algo, will consider those path which req minimum effort.
        """

        m,n = len(heights), len(heights[0])
        # create dist 2D array with n cols and m rows 
        dist = [[float("inf")]*n for _ in range(m)]
        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        dist[0][0] = 0

        pq = [(0,0,0)] # row, col, effort 

        while pq:
            row, col, prev_effort = hq.heappop(pq)
            # remove redundant cells
            if prev_effort > dist[row][col]:
                continue
            
            # dijkstra gurantees reaching destination with minimum effort as it is greedy in choosing the minimum effort path 
            if row == m-1 and col == n-1:
                return dist[row][col]
            
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < m and 0 <= nc < n:
                    curr_effort = abs(heights[nr][nc] - heights[row][col])
                    new_effort = max(prev_effort, curr_effort)

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        hq.heappush(pq, (nr,nc, new_effort))

        return 0
