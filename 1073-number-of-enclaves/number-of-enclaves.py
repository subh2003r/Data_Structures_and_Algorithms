from collections import deque

class Solution:
    def bfs_way(self, grid):
        dq = deque()
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        count_landCells = 0

        for row in range(m):
            for col in range(n):
                if row == 0 or row == m-1 or col == 0 or col == n-1:
                    if grid[row][col] == 1:
                        dq.append((row,col))
                        grid[row][col] = -1  # '-1' -> land can reach off boundary

        while dq:
            row, col = dq.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = -1        # connected grid cell '1' which can reach off boundary
                    dq.append((nr, nc))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    count_landCells += 1
        
        return count_landCells

                    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        return self.bfs_way(grid)