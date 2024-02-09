# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current_node = head
        while current_node:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
        return prev
