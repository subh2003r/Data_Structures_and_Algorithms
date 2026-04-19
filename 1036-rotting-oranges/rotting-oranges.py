from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n  = len(grid), len(grid[0])
        dq = deque()
        # count of all fresh oranges
        fresh = 0
        # minimum time taken 
        time_taken = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    dq.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        

        while dq and fresh > 0:
            for _ in range(len(dq)):
                row, col = dq.popleft()
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1

                        dq.append((nr, nc))

            time_taken += 1
        
        return time_taken if fresh == 0 else -1