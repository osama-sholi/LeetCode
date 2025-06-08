# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        result = ListNode()
        current = result
        while True:
            min_l = 0
            for i in range(len(lists)):
                if (not lists[min_l]) or (lists[i] and (lists[i].val < lists[min_l].val)):
                    min_l = i
            if not lists[min_l]:
                return result.next
            current.next = lists[min_l]
            current= current.next
            lists[min_l] = lists[min_l].next

