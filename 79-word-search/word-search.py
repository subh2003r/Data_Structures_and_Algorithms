class Solution:
    def __init__(self):
        self.m = 0 # no of columns
        self.n = 0 # no of rows
        self.dir = [(0,1),(0,-1),(-1,0),(1,0)]

    def findPath(self,board,word,index,curr_i,curr_j):
        if index == len(word):
            return True

        if curr_i < 0 or curr_i >= self.n or curr_j < 0 or curr_j >= self.m:
            return False

        if board[curr_i][curr_j] == "$":
            return False

        if board[curr_i][curr_j] != word[index]:
            return False

        store_temp = board[curr_i][curr_j]
        board[curr_i][curr_j] = "$"

        for val in self.dir:
            new_i = curr_i + val[0]
            new_j = curr_j + val[1]

            if self.findPath(board,word,index+1,new_i,new_j) == True:
                return True

        board[curr_i][curr_j] = store_temp

        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board[0])
        self.n = len(board)

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0] and self.findPath(board,word,0,i,j):
                    return True
        
        return False