# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q = deque([root])
        serial = []

        while q:
            node = q.popleft()
            if not node:
                serial.append("null")
            else:
                serial.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        # remove training "null"
        while serial and serial[-1] == "null":
            serial.pop()
        
        return ",".join(serial)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data.strip() == "":
            return None

        serial = data.split(",")
        n = len(serial)

        rootVal = int(serial[0])
        root = TreeNode(rootVal)
        q = deque([root])

        index = 0

        while q and index < n:
            node = q.popleft()
            left, right = 2*index+1, 2*index+2

            if left < n and serial[left] != "null":
                node.left = TreeNode(int(serial[left]))
                q.append(node.left)
            if right < n and serial[right] != "null":
                node.right = TreeNode(int(serial[right]))
                q.append(node.right)
            
            index += 1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))