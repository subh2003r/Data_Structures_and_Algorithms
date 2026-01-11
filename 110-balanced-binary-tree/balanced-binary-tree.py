# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Brute force approach 
        def height(root):
            if not root:
                return 0
            
            lh = height(root.left)
            rh = height(root.right)
            
            return 1 + max(lh,rh)

        def traversal(root):
            if not root:
                return True

            leftHeight = height(root.left)
            rightHeight = height(root.right)

            # checking is done before because if the parent node is unbalanced then straight-away return False, so the cost of operation to check lower node wont get counted
            if abs(leftHeight-rightHeight) > 1:
                return False

            return traversal(root.left) and traversal(root.right)


        return traversal(root)