"""
Disjoint Set implemetation 
Union-find --> 
UNION-FIND (DISJOINT SET) – QUICK SUMMARY

1. What is Union-Find?
- A data structure used to manage groups (sets) of elements.
- Helps to:
  • Merge two groups
  • Check if two elements belong to the same group

--------------------------------------------------

2. Core Operations

a) Find (findParent)
- Returns the leader (root) of the group.
- Used to identify which group an element belongs to.

b) Union
- Merges two groups into one.

Types:
- Union by Size → smaller group joins larger group
- Union by Rank → shorter tree joins taller tree

--------------------------------------------------

3. Key Optimizations

a) Path Compression
- While finding root, make nodes directly point to root.
- Makes future operations faster.

b) Union by Rank/Size
- Keeps tree shallow → improves efficiency.

--------------------------------------------------

4. Time Complexity

- Almost O(1) per operation
- More precisely: O(α(n)) (very small, near constant)

--------------------------------------------------

5. Why it helps

Without DSU:
- Connectivity check → BFS/DFS → O(V + E)

With DSU:
- Connectivity check → near O(1)

--------------------------------------------------

6. Where is it used?

- Graph connectivity problems
- Kruskal’s Minimum Spanning Tree
- Detecting cycles in graphs
- Counting connected components
- Dynamic graph problems
- Grid problems (Number of Islands)

--------------------------------------------------

7. Final Intuition

- Each group has a leader (root)
- Find → tells the leader
- Union → merges groups
- Path compression → speeds up find

--------------------------------------------------

ONE LINE MEMORY:
Union merges groups, Find checks if two elements are in the same group.

"""
"""
class DisjointSet:
    def __init__(self, n: int):
        # all nodes are independent groups -- i.e parent of their own 
        # size -> number of nodes present
        # rank -> height of the tree
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        self.rank = [0]*n

    def findParent(self, node):
        if self.parent[node] == node:
            return self.parent[node]
        
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)        

    def unionByRank(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)

        # parents of both nodes are same 
        if pu == pv:
            return
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
     
    def unionBySize(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return 
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        elif self.size[pv] < self.size[pu]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
"""

from collections import defaultdict

class Solution:
    def component_find(self, vertex, visited, graph):
        components = 0
        def dfs(node):
            visited[node] = True
            for neighb in graph[node]:
                if not visited[neighb]:
                    dfs(neighb)

        for node in range(vertex):
            if not visited[node]:
                components += 1
                dfs(node)

        return components

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph = defaultdict(list)

        visited = [False]*n
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        return self.component_find(n, visited, graph) - 1
        

        
