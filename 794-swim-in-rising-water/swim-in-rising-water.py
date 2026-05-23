import heapq as hq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        visited = set()
        # store (time, row, col)
        heap = [(grid[0][0], 0, 0)]

        while heap:
            time, row, col = hq.heappop(heap)
            if (row, col) in visited:
                continue # heap gurantees that minimum cost to reach this (row,col), so rejecting other path which costs more than earlier cost
            
            if row == n-1 and col == m-1:
                return time 

            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < n and 0 <= nc < m:
                    new_time = max(time, grid[nr][nc])
                    hq.heappush(heap, (new_time, nr, nc))
        
        return -1
