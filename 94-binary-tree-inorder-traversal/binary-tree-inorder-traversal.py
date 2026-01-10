# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative approach
        if root is None:
            return []

        stack = []
        curr = root

        while curr or stack:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            top = stack.pop()
            self.result.append(top.val)

            curr = top.right
        
        return self.result

        """
        # recursive approach 
        if root is None:
            return []
        
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)

        return self.result
        """