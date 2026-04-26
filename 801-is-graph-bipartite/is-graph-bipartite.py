from collections import deque

class Solution:
    def __init__(self):
        self.color = None

    def bfs_approach(self, graph, node):
        dq = deque([node])
        """
        Assign either 0 or 1 color to the nodes
        """
        self.color[node] = 0
        # Traverse each nodes 
        while dq:
            node = dq.popleft()
            for neighb in graph[node]:
                # this means node is not visited 
                if self.color[neighb] == -1:
                    self.color[neighb] = 1 - self.color[node] # flip the color
                    dq.append(neighb)
                else:
                    # neighbour already visited -- color for neighb already marked 
                    if self.color[neighb] == self.color[node]:
                        # parent and children node have same color -- node connected via same edge have same color -- not bipartite
                        return False
        
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        If the graph can be colored in atmost two colors then it is bipartite.
        Graph can be disconnected --> Graph has multiple components 
        A component having single node is also bipartite
        """
        n = len(graph)
        self.color = [-1]*n

        """
        Iterate through all the components in the graph and start traversing from those which is not visited .. here visited is denoted by color array which if -1 says color/visited is not asssinged else color/visited is assigned
        """

        for node in range(n):
            if self.color[node] == -1:
                if not self.bfs_approach(graph, node):
                    return False
        
        return True


        