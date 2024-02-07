# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        current = dummy

        while head:
            total_sum = 0
            if head.val==0:
                head = head.next
            while head.val !=0:
                total_sum += head.val
                head = head.next
            current.next = ListNode(total_sum)
            current = current.next
            head = head.next
        return dummy.next