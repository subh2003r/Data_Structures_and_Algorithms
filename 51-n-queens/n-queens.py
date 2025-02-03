class Solution:
    def __init__(self):
        self.result = []

    def isPossible(self,board,row,col,n):
        # checking the above columns
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # checking the upper left diagonals
        new_row, new_col = row-1,col-1
        while new_row >= 0 and new_col >= 0:
            if board[new_row][new_col] == 'Q':
                return False
            new_row -= 1
            new_col -= 1

        # checking the upper right diagonals
        new_row, new_col = row-1,col+1
        while new_row >= 0 and new_col < n:
            if board[new_row][new_col] == 'Q':
                return False
            new_row -= 1
            new_col += 1

        return True

    def findWays(self,board,n,row):
        if row == n:
            self.result.append(["".join(val) for val in board])
            return

        for col in range(n):
            if self.isPossible(board,row,col,n):
                board[row][col] = 'Q' # safe configuration to place the queen 
                self.findWays(board,n,row+1)
                board[row][col] = '.'  # backtrack

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        self.findWays(board,n,0)
        return self.result