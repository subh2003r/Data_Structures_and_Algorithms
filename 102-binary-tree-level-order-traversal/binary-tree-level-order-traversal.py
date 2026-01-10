# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def __init__(self):
        self.q = Queue()
        self.result = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        self.q.put(root)

        while not self.q.empty():
            size = self.q.qsize()
            level = []

            for i in range(size):
                node = self.q.get()
                level.append(node.val)
                if node.left:
                    self.q.put(node.left)
                if node.right:
                    self.q.put(node.right)
            
            self.result.append(level)
        
        return self.result