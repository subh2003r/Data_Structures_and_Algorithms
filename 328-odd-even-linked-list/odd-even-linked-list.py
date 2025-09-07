# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        odd_head, even_head = head, head.next if head else None

        # storing all odd nodes in list
        while odd_head and odd_head.next:
            res.append(odd_head.val)
            odd_head = odd_head.next.next

        if odd_head:
            res.append(odd_head.val)

        # storing all even nodes in list
        while even_head and even_head.next:
            res.append(even_head.val)
            even_head = even_head.next.next
        
        if even_head:
            res.append(even_head.val)

        curr = head
        index = 0

        while curr:
            curr.val = res[index]
            index += 1
            curr = curr.next

        return head