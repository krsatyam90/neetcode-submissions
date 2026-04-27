# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers:
        # 'prev' to track the previous node (initialized to None since the first node's next will be None),
        # 'cur' to track the current node (starting with the head of the list).
        prev, cur = None, head 

        # Iterate through the list until 'cur' becomes None (end of the list).
        while cur:
            # Temporarily store the next node in 'nxt' to avoid losing reference to the remaining list.
            nxt = cur.next 
            
            # Reverse the direction of the current node's pointer to point to the previous node.
            cur.next = prev 
            
            # Move the 'prev' pointer forward to the current node.
            prev = cur 
            
            # Move the 'cur' pointer forward to the next node in the original list.
            cur = nxt 
        
        # Return the new head of the reversed list, which is the last non-None 'prev'.
        return prev

        
        