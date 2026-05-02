"""
** Topological Sort **:

Two Methods:- DFS vs BFS
1. DFS Topo (Depth First)
Go deep -> Finish all dependencies -> then add node 
"push after dependencies"

2. BFS Topo (Breadth First)
Start with Nodes having no dependencies -> remove them -> unlock others 
"process nodes only when they have no pending prerequisites"
"""

"""
** Find Shortest path **

1. Given, Unit weight across all edges in graph
    -> Done via BFS level wise traversal 

2. Given, Distinct weight across all edges in DAG (Directed Acyclic Graph)
    -> Find Topological Ordering of nodes
    -> And, then process those nodes in that order 
    -> This will allow proper edge weights to be passed further, thus minimizing multiple 
    relaxation across edges

3. Given, Distinct weight across edges in Graph 
    -> Dijkstra algo (Greedy Based, priority queue)
    -> Bellman ford algo (DP, works for negative edges as well)

"""

"""
Time complexity:
1. For DAG (using Topo sort + BFS/DFS) -> O(V+E)
2. For Dijkstra (Greedy + priority queue + relaxation of edges) -> O(ElogV)
3. For Bellman Ford (for negative edges in graph) -> O(V*E)
"""
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        n, m = len(grid), len(grid[0])

        directions = [(-1,0),(0,-1),(0,1),(1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
        dq = deque([(0,0,1)])

        # make 0 -> -1, which will mark it as unvisited 
        for row in range(n):
            for col in range(m):
                grid[row][col] = -1 if grid[row][col] == 0 else grid[row][col]

        while dq:
            row, col, length = dq.popleft()
            # BFS solution -- reaches faster (through shortest path)
            if row == n-1 and col == m-1:
                return length

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == -1:
                    grid[nr][nc] = 0 # mark as visited 
                    new_length = length + 1
                    dq.append((nr, nc, new_length))

        # no valid path found
        return -1
                
