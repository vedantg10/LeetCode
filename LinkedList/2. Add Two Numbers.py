# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.reverseNumber(l1)
        number2 = self.reverseNumber(l2)
        final_sum =  number1 + number2
        dummy_head = ListNode()
        current = dummy_head

        # Convert the sum to a linked list
        for digit in str(final_sum)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy_head.next


        
    
    def reverseNumber(self,l1: Optional[ListNode]):
        current_node = l1
        number = ""
        reverse_number = 0
        while current_node:
            number += str(current_node.val)
            current_node = current_node.next
        while int(number)>0:
            last_digit = int(number)%10
            reverse_number = reverse_number*10 + last_digit
            number = int(number)//10
        return reverse_number