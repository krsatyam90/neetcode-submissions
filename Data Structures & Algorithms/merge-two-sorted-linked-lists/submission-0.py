# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = node = ListNode()

        # Traverse both lists until one is exhausted
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val < list2.val:
                # If list1's value is smaller, append it to the merged list
                node.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # If list2's value is smaller or equal, append it to the merged list
                node.next = list2
                # Move to the next node in list2
                list2 = list2.next

            # Move the node pointer to the next position in the merged list
            node = node.next

        # If list1 still has remaining nodes, append them to the merged list
        if list1:
            node.next = list1
        # If list2 still has remaining nodes, append them to the merged list
        elif list2:
            node.next = list2

        # The merged list starts at dummy.next (skipping the dummy node)
        return dummy.next



                
        