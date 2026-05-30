import heapq as  hq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]

        visited = [[False]*n for _ in range(m)]

        directions = [(0,1), (1,0)]

        while pq:
            path, i, j = hq.heappop(pq)
            if i == m-1 and j == n-1:
                return path
                        
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    hq.heappush(pq, (path+grid[nr][nc], nr, nc))
                    visited[nr][nc] = True
            
        return -1