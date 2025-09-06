# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
    “When slow and fast meet, fast has run extra full loops inside the cycle. The distance  slow covered from head to the meeting point is L + x, and fast has covered the same plus full cycles. The extra distance is always a multiple of the cycle length. So, if we move one pointer back to head and keep the other at the meeting point, and now move both one step at a time, the extra cycle distance cancels out, and they will meet exactly at the cycle's starting node.”
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return fast
        
        return None
        
