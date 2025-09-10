# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev_node = None

        def getKthNode(node, x):
            x -= 1
            while node and x > 0:
                node = node.next
                x -= 1
                
            return node

        def reverse(left):
            prev, curr = None, left
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        while curr:
            kthNode = getKthNode(curr, k)

            if kthNode is None:
                prev_node.next = curr
                break

            next_node = kthNode.next
            kthNode.next = None

            temp_head = reverse(curr)

            if curr == head:
                head = temp_head

            if prev_node:
                prev_node.next = temp_head

            prev_node = curr
            curr = next_node
        
        return head

        