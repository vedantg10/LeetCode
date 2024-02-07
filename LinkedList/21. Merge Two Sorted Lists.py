# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        dummy = ListNode(0)
        current = dummy

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next
            current = current.next

        # If one of the lists is not exhausted, link the remaining nodes
        current.next = pointer1 or pointer2

        return dummy.next
     