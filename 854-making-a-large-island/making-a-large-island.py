class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        
        return self.parent[u]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return 
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ds = DisjointSet(n*m)

        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        totalIsland = 0

        # Connect all existing islands 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                
                totalIsland += 1
                node = i*m + j
                
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc 
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        adjNode = nr*m + nc
                        ds.union(node, adjNode)
        

        # flip each 0's and check the area -- do not modify 0's inplace 
        res = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    continue
                
                parents = set()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc 
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        adjNode = nr*m + nc
                        parents.add(ds.find(adjNode))
                
                # sum of size of unique parent islands from each neighbouring connected islands + 1 flipped island
                islandSize = 1
                for component in parents:
                    islandSize += ds.size[component]
                
                res = max(res, islandSize)
        
        return res if totalIsland != n*m else totalIsland


                
