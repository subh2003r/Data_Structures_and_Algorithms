# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodeA, nodeB = l1, l2
        dummy = ListNode()
        curr = dummy
        carry = 0

        while nodeA or nodeB or carry:
            sum_val = 0
            if nodeA:
                sum_val += nodeA.val
                nodeA = nodeA.next
            if nodeB:
                sum_val += nodeB.val
                nodeB = nodeB.next
            
            if carry:
                sum_val += carry
            
            curr.next = ListNode(sum_val % 10)
            carry = sum_val // 10
            curr = curr.next
        
        return dummy.next