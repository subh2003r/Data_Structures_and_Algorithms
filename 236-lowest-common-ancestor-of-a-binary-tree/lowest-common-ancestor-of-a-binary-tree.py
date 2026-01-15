# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Brute force approach 
        if not root:
            return None

        def findPath(node, searchNode, path):
            if not node:
                return False

            path.append(node)
            if node == searchNode:
                return True
            
            if findPath(node.left, searchNode, path):
                return True
            if findPath(node.right, searchNode, path):
                return True

            path.pop()

        pPath = []
        qPath = []
        findPath(root, p, pPath)
        findPath(root, q, qPath)

        i,j = 0, 0
        lastVisited = None
        while i < len(pPath) and j < len(qPath):
            if pPath[i] != qPath[j]:
                break
            lastVisited = pPath[i]
            i += 1
            j += 1

        return lastVisited
