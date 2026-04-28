class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        completedCourses = []
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
            completedCourses.append(task)

            for neighb in graph[task]:
                indegree[neighb] -= 1
                if indegree[neighb] == 0:
                    # all dependency completed, now we can proceed to complete this current task -- so getting appended in queue
                    dq.append(neighb)
        
        return completedCourses if len(completedCourses) == numCourses else []