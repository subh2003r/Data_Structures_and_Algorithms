"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1st approach using HashMaps
        store_node = {}
        copy_head = head

        while copy_head:
            new_node = ListNode(copy_head.val)
            store_node[copy_head] = new_node

            copy_head = copy_head.next

        new_head = None
        copy_head = head

        while copy_head:
            node = store_node[copy_head]
            if new_head == None:
                new_head = node

            node.next = store_node.get(copy_head.next, None)
            node.random = store_node.get(copy_head.random, None)

            copy_head = copy_head.next

        return new_head
            
