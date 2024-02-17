# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        while(current and current.next):
            pairNode = current.next.next
            second = current.next
            second.next = current
            current.next = pairNode
            prev.next = second
            prev = current
            current = pairNode
        return dummy.next

        