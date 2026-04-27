# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists where each node contains a single digit.
        The digits are stored in reverse order (1's place at the head), and the result is also
        returned as a linked list in the same format.
        
        :param l1: Head of the first linked list.
        :param l2: Head of the second linked list.
        :return: Head of the linked list representing the sum.
        """
        # Dummy node to serve as the starting point of the result linked list
        dummy = ListNode()
        cur = dummy  # Pointer to construct the new linked list
        carry = 0  # Variable to handle carry-over during addition

        # Continue the loop as long as there are digits left in l1, l2, or there is a carry
        while l1 or l2 or carry:
            # Extract values from l1 and l2; use 0 if the list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry
            val = v1 + v2 + carry
            carry = val // 10  # Determine the new carry (1 if sum >= 10, else 0)
            val = val % 10  # Extract the digit to store in the current node

            # Create a new node for the current digit and link it to the result list
            cur.next = ListNode(val)
            cur = cur.next  # Move the pointer forward in the result list

            # Move to the next nodes in l1 and l2, if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the head of the result list (skipping the dummy node)
        return dummy.next 
