from collections import defaultdict 
import heapq as hq 

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for u,v, wt in roads:
            graph[u].append((v,wt))
            graph[v].append((u,wt))

        dist = [float("inf")]*n
        ways = [0]*n
        dist[0] = 0
        ways[0] = 1

        src = 0
        pq = [(0, src)]   # (time, node)

        while pq:
            time, node = hq.heappop(pq)
            # skip outdated entries 
            if time > dist[node]:
                continue

            for neighb, wt in graph[node]:
                new_time = time + wt

                if new_time < dist[neighb]:
                    dist[neighb] = new_time
                    ways[neighb] = ways[node]
                    hq.heappush(pq, (new_time, neighb))

                elif new_time == dist[neighb]:
                    ways[neighb] = (ways[neighb] + ways[node]) % MOD
        
        return ways[n-1]