import heapq as hq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        If we reach a node first in priority queue, then the distance it takes to reach that node is already minimum, because priority queue takes into consideration the shortest path -- minimum cost, at a given time/future. Thus, it gurantees minimal path/cost for a node.
        """
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
          
        dist = {} # store (node, cost/time)
        src = k
        pq = [(0, src)] # store (time, node)
        
        while pq:
            time, node = hq.heappop(pq)
            # pruning condition -- minimize the search space 
            if node in dist:
                continue
            
            dist[node] = time
            for neighb, weight in graph[node]:
                if neighb not in dist:
                    hq.heappush(pq, (time+weight, neighb))

        # check whether all nodes are reached or not i.e signals to all nodes are reached or not 
        if len(dist) != n:
            return -1
        
        return max(dist.values())