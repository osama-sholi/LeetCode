# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        current1 = l1
        current2 = l2
        result: Optional[ListNode] = None
        current3: Optional[ListNode] = None
        while current1 != None or current2 != None:
            val1 = getattr(current1, 'val', 0)
            val2= getattr(current2, 'val', 0)
            csum = val1 + val2 + reminder
            newNode = ListNode(csum % 10, None)
            reminder = csum // 10
            if result is None:
                current3 = newNode
                result = current3
            else:
                current3.next = newNode
                current3 = current3.next
            current1 = getattr(current1, 'next', None)
            current2 = getattr(current2, 'next', None)
        
        current3.next = ListNode(reminder,None) if reminder > 0 else None
        return result


            
            