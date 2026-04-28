"""
Topological sort is an ordering of nodes in directed graph such that:
for every directed edge u -> v, 'u' comes before 'v' in the ordering

Topological sort is only possible in "Directed Acyclic Graph (DAG)"
    If there is a cycle, no valid ordering exists

    Intuition:
    Think of task as an dependencies 
    'Do A before B'
    'Do B before C'

    Ordering looks like -> 'A -- B -- C'
"""

"""
Kahn's algorithm

1. Find out nodes with indegree 0 (nodes having no dependency should come first)
2. push all indegree 0 nodes into queue
3. iterate through the neighbours of node, and decrement indegree by 1 (this is done because current node dependency is done and since it is done, the neighbour dependency by 1 gets reduced)
4. Check for cycle in the graph, if "yes" then no ordering is formed

"""

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        completedTask = 0
        dq = deque()

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        # append indegree as 0 -> task with no dependency should be completed first 
        for node in range(numCourses):
            if indegree[node] == 0:
                dq.append(node)

        while dq:
            task = dq.popleft()
            completedTask += 1

            for neighb in graph[task]:
                indegree[neighb] -= 1
                if indegree[neighb] == 0:
                    # all dependency completed, now we can proceed to complete this current task -- so getting appended in queue
                    dq.append(neighb)
        
        return True if completedTask == numCourses else False



                