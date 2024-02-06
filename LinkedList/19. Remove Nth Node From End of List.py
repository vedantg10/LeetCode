# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer1 = dummy
        pointer2 = head
        for _ in range(n):
            pointer2 = pointer2.next
        while(pointer2):
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        pointer1.next = pointer1.next.next
        return dummy.next



        