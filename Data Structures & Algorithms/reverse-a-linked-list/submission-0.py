# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Iteration
        # Initialize two pointers: prev (to store the previous node, initially None)
        # and curr (to traverse the list, starting at the head)
        prev = None
        curr = head

        # Traverse the linked list until the end
        while curr:
            # Store the next node in a temporary variable
            nxt = curr.next
            # Reverse the current node's pointer to point to the previous node
            curr.next = prev
            # Move the prev pointer to the current node
            prev = curr
            # Move the curr pointer to the next node in the original list
            curr = nxt
        
        # At the end of the loop, prev will point to the new head of the reversed list
        return prev
        

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Base case: If the list is empty (head is None), return None
#         if not head:
#             return None
        
#         # Initialize newHead as the current head (this will eventually point to the new head of the reversed list)
#         newHead = head
        
#         # Recursive case: If there is a next node, continue reversing
#         if head.next:
#             # Recursively reverse the rest of the list
#             newHead = self.reverseList(head.next)
            
#             # Set the next node's next pointer to the current node (reverse the link)
#             head.next.next = head
        
#         # Break the current node's link to avoid cycles (set it to None)
#         head.next = None

#         # Return the new head of the reversed list
#         return newHead

        
        