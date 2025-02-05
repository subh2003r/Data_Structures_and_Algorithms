# User function Template for python3

class Solution:
    def __init__(self):
        self.assign = []
        self.edges = []
        self.v = 0
        
    # isPossible() function checks whether the vertex can be assigned with the colour
    # return true if properly assigned else false
    
    def isPossible(self,vertex,colour):
        for node in range(self.v):
            if (node,vertex) in self.edges or (vertex,node) in self.edges:
                if self.assign[node] != -1 and self.assign[node] == colour:
                    return False
                    
        return True
    
    def recur(self,curr_vertex,m):
        if curr_vertex == self.v:
            return True    # successfully coloured all vertices
            
        for i in range(m):
            if self.isPossible(curr_vertex,i):
                self.assign[curr_vertex] = i
                if self.recur(curr_vertex+1,m):
                    return True
                self.assign[curr_vertex] = -1 # backtrack
        
        return False   # if no valid color found then backtrack
                
    def graphColoring(self, v, edges, m):
        # code here
        self.assign = [-1]*v
        self.edges = edges
        self.v = v
        return self.recur(0,m)

#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges_input = list(map(int, input().split()))
        m = int(input())
        edges = []

        # Populate the edges list with edge pairs
        for i in range(0, len(edges_input), 2):
            edges.append((edges_input[i], edges_input[i + 1]))

        solution = Solution()
        print("true" if solution.graphColoring(n, edges, m) else
              "false")  # Call the graph coloring function
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends