# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left_head, right_head):
            dummy = ListNode()
            tail = dummy

            while left_head and right_head:
                if left_head.val <= right_head.val:
                    tail.next = left_head
                    left_head = left_head.next
                else:
                    tail.next = right_head
                    right_head = right_head.next
                
                tail = tail.next
        
            if left_head:
                tail.next = left_head
            else:
                tail.next = right_head

            return dummy.next

        def findMiddle(head):
            # modifying the tortoise-hare algo, so that middle link gets broken
            slow,fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def mergeSort(head):
            if not head or not head.next:
                return head
            
            # find middle node
            mid = findMiddle(head)  
            right_head = mid.next
            mid.next = None

            left_head = head

            left_head = mergeSort(left_head)   
            right_head = mergeSort(right_head)

            return merge(left_head, right_head)

        return mergeSort(head)