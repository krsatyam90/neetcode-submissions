# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers: 
        # slow moves one step at a time, and fast moves two steps at a time
        slow, fast = head, head

        # Traverse the list as long as fast and fast.next are not None
        while fast and fast.next:
            # Move slow pointer one step ahead
            slow = slow.next
            # Move fast pointer two steps ahead
            fast = fast.next.next
            
            # If slow and fast pointers meet, a cycle is detected
            if slow == fast:
                return True
        
        # If we exit the loop, it means no cycle exists
        return False




        