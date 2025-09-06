# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, next_node = None, head, head

        while next_node != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev