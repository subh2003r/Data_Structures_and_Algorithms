# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        zigZag = []

        # initialize queue with root node of the tree
        q.append(root)
        index = 0

        while q:
            size = len(q)
            res = []

            for i in range(size):
                node = q.popleft()
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            
            if index % 2:
                res.reverse()
            
            zigZag.append(res)
            
            index += 1
        
        return zigZag