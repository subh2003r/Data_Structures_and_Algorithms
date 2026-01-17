# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leftHeight(self, node):
        height = 0
        while node:
            node = node.left
            height += 1
        
        return height 
    
    def rightHeight(self, node):
        height = 0
        while node:
            node = node.right
            height += 1
        
        return height 
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        find the extensive left and right height of the sub-trees, if both are equal then the subtree is complete binary tree else recursively go to each level and calculate the count of trees
        Recursive calls happen at less than/ approx O(logn)
        Whenever a subtree is perfect, we stop immediately there (no deeper recursion).
        Height calculation = O(logn) for left and right subtrees 

        Overall time complexity: O(logn*logn) = O(log2n)
        """

        if not root:
            return 0

        left = self.leftHeight(root)
        right = self.rightHeight(root)

        if left == right:
            return 2**left-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        