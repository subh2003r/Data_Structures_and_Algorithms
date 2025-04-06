class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        small = big = prev = None

        def inorder(r):
            nonlocal small, big, prev
            if not r:
                return
            inorder(r.left)
            if prev and prev.val > r.val:
                small = r
                if not big:
                    big = prev
            prev = r
            inorder(r.right)

        inorder(root)
        small.val, big.val = big.val, small.val