# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        store = []
        for head in lists:
            iteri = head
            while head:
                store.append(head.val)
                head = head.next
        
        store.sort()

        new_head = None
        temp = None
        
        for value in store:
            node = ListNode(value)
            if new_head is None:
                new_head = node
                temp = new_head
            else:
                temp.next = node
                temp = temp.next
        
        return new_head

            