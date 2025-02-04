#User function Template for python3
class Solution:
    def __init__(self):
        self.n = 0 # no of rows
        self.direc = {(1,0):'D',(0,-1):'L',(0,1):'R',(-1,0):'U'}
        self.result = []
    
    # Function to find all possible paths
    def recur(self,mat,curr_i,curr_j,subPath):
        if curr_i == self.n-1 and curr_j == self.n-1:
            self.result.append(subPath)
            return
        
        if curr_i < 0 or curr_j < 0 or curr_i >= self.n or curr_j >= self.n:
            return
        
        if mat[curr_i][curr_j] == -1 or mat[curr_i][curr_j] == 0:
            return
        
        store_temp = mat[curr_i][curr_j]
        mat[curr_i][curr_j] = -1  # marking the current path as visited
        
        for key,value in self.direc.items():
            new_i = curr_i + key[0]
            new_j = curr_j + key[1]
            self.recur(mat,new_i,new_j,subPath+value)
        
        mat[curr_i][curr_j] = store_temp
   
    def findPath(self, mat):
        # code here  
        self.n = len(mat)
        self.recur(mat,0,0,"")
        
        return self.result
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends