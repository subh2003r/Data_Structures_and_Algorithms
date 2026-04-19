class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        visited = [False]*n

        # creating adjacency list
        adj = [[] for _ in range(n)]

        for row in range(n):
            for col in range(n):
                if row != col and isConnected[row][col] == 1:
                    # considering undirected edges
                    adj[row].append(col) 
                    adj[col].append(row)

        def dfs(vertex):
            visited[vertex] = True

            for neighb in adj[vertex]:
                if not visited[neighb]:
                    dfs(neighb)

        for vertex in range(n):
            if not visited[vertex]:
                dfs(vertex) 
                provinces += 1

        return provinces

                    

        