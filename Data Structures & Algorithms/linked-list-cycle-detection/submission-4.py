# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow , fast = head , head
        # while fast and fast.next:
        #     slow = slow.next 
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True 
        # return False
        # Initialize two pointers: 'slow' and 'fast', both starting at the head of the list.
        # 'slow' moves one step at a time, while 'fast' moves two steps at a time.
        slow, fast = head, head

        # Traverse the linked list with the two pointers.
        while fast and fast.next:
            # Move 'slow' one step ahead.
            slow = slow.next
            # Move 'fast' two steps ahead.
            fast = fast.next.next

            # If 'slow' and 'fast' meet, it means there is a cycle in the list.
            if slow == fast:
                return True

        # If the loop ends, it means no cycle exists in the list.
        return False

         
        