# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        size = 0
        while current:
            current = current.next
            size += 1
        
        if size - n == 0:
            return head.next
        
        current = head
        for i in range(size - n - 1):
            current = current.next
        print(current)
        current.next = (current.next).next
        return head


