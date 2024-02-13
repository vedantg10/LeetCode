# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while(fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        prev = None
        while(slow_pointer):
            temp = slow_pointer.next
            slow_pointer.next = prev
            prev = slow_pointer
            slow_pointer = temp
        left_pointer = head
        right_pointer = prev
        while(right_pointer):
            if left_pointer.val != right_pointer.val:
                return False
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        return True




        