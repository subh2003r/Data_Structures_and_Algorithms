# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxPath = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def findPath(root):
            if not root:
                return 0
            
            leftPath = findPath(root.left)
            rightPath = findPath(root.right)
            
            currPathSum = root.val + (0 if leftPath < 0 else leftPath) + (0 if rightPath < 0 else rightPath)
            self.maxPath = max(self.maxPath, currPathSum)

            return root.val + max(0,leftPath, rightPath)


        findPath(root)

        return self.maxPath