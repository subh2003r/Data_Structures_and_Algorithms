# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root

        curr = root

        while curr:
            if curr.val < val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left

        return root
