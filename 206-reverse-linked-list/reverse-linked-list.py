# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # iterative approach

        prev, curr, next_node = None, head, head

        while next_node != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
        '''

        # recursive approach 

        
        def reverse(node):
            if node is None or node.next is None:
                return node
            
            new_head = reverse(node.next)
            front = node.next
            front.next = node
            node.next = None

            return new_head

        return reverse(head)