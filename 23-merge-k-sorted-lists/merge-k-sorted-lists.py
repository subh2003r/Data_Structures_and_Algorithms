# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # function to merge 2 lists 
        def merge2List(head1, head2):
            if head1 is None:
                return head2
            
            if head2 is None:
                return head1

            temp_head = ListNode(0, None)
            iteri = temp_head
            
            while head1 and head2:
                if head1.val <= head2.val:
                    iteri.next = head1
                    head1 = head1.next
                else:
                    iteri.next = head2
                    head2 = head2.next
                
                iteri = iteri.next

            # merge remaining parts
            iteri.next = head1 if head1 else head2

            return temp_head.next

        if not lists:
            return None

        head = None
        for l in lists:
            head = merge2List(head, l)

        return head

        """
        # Brute force approach 
        # Time complex: O(m) + O(mlogm) + O(m) where m = n*k
        # Space complex: O(m) + O(m)

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
        """

            