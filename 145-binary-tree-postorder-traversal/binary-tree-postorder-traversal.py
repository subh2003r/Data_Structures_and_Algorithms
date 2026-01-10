# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root 
        lastVisited = None 

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                # if right subtree exists and has not been processed yet
                if peek.right and peek.right != lastVisited:
                    curr = peek.right
                else:
                    node = stack.pop()
                    self.result.append(node.val)
                    lastVisited = node

        return self.result
            
        """
        # recursive approach 
        if root is None:
            return []

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)

        return self.result
        """