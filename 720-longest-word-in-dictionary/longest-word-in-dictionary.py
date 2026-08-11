class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    """
    Time complex: O(NL), where N = total no of words, L = Length of word
    """
    def longestWord(self, words: List[str]) -> str:
        res = ""
        self.root = Node()

        for word in words:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                
                node = node.children[ch]

            node.isEnd = True
        
        
        def dfs(node, current):
            nonlocal res

            if len(current) > len(res):
                res = current
            elif len(current) == len(res):
                res = min(res, current)

            for child in node.children:
                ch = node.children[child]

                if ch.isEnd:
                    dfs(ch, current + child)


        dfs(self.root, "")
        
        return res