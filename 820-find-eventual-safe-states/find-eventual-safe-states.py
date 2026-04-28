from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        A node which is part of a cycle, can never be safe node as it can never reach a terminal node.
        Reason:-
        A terminal node means, a node with no outgoing edges 
        But in a cycle:
        - Every node has atleast one outgoing edge
        - So you are never forced to stop 

        The key condition that fails for node in cycle path:-
        - In a cycle, there exists atleast one path that never ends 
        That alone makes the node unsafe

        Intuition:-
        - Safe Node: All roads lead to dead-end
        - Cycle Node: There exists a road where you keep driving forever 
        Even if one such infinite path exists, the node is unsafe

        """
        # Reverse topological order + BFS
        dq = deque()
        v = len(graph)
        safe = [False]*v
        outdegree = [0]*v
        reverse_graph = [[] for _ in range(v)]

        # construct reverse-graph with child --> parent relationship
        for node in range(v):
            outdegree[node] = len(graph[node])
            # start from terminal nodes 
            if outdegree[node] == 0:
                dq.append(node)

            for neighb in graph[node]:
                reverse_graph[neighb].append(node)

        while dq:
            node = dq.popleft()
            # mark node as safe -- already processed 
            safe[node] = True

            for parent in reverse_graph[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    dq.append(parent)

        # collect all safe nodes
        return [node for node in range(v) if safe[node]]