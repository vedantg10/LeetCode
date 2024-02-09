# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # temp_set = set()
        while head and head.val== val:
            head = head.next
        prev = None
        current_node = head
        while current_node:
            if (current_node.val != val):
                prev = current_node
                current_node = current_node.next
            else:
                prev.next = prev.next.next
                current_node = current_node.next
        return head
