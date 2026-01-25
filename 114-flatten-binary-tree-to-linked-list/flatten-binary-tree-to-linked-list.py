# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Do reverse preorder traversal to keep count of previous Node
        # store Previous Node
        # Time complex: O(N) and Space complex: O(N) recursion stack
        prev = None

        def interchangeLink(node):
            nonlocal prev
            if not node:
                return 
            
            interchangeLink(node.right)
            interchangeLink(node.left)

            node.right = prev
            node.left = None
            prev = node

        interchangeLink(root)
        return root
         
