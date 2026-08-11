class Node:
    def __init__(self):
        self.children = {}
        self.wordFound = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n,m = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
        res = []

        # build Trie
        self.root = Node()

        for word in words:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                
                node = node.children[ch]
            
            node.wordFound = word
        
        def dfs(node, r, c):
            ch = board[r][c]
            if ch not in node.children:
                return 

            child = node.children[ch]

            if child.wordFound:
                res.append(child.wordFound)
                child.wordFound = None # prevents duplicacy of adding the same word multiple times

            # done to prevent further iteration over the same cell 
            board[r][c] = "#"

            for dr, dc in directions:
                nr, nc = dr+r, dc+c 
                if 0 <= nr < n and 0 <= nc < m:
                    if board[nr][nc] != "#":
                        dfs(child, nr, nc)

            # Backtrack -- restoring original characters
            board[r][c] = ch

        # iterate over the entire cell 
        for row in range(n):
            for col in range(m):
                dfs(self.root, row, col)

        return res            
        


