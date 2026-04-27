# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = Node = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         Node.next = list1
        #         list1 = list1.next
        #     else:
        #         Node.next = list2
        #         list2 = list2.next
        #     Node = Node.next

        # if list1:
        #     Node.next = list1
        # elif list2:
        #     Node.next = list2
        # return dummy.next


        # Create a dummy node to serve as the starting point for the merged list.
        # 'node' is a pointer to build the new list.
        dummy = node = ListNode()

        # Iterate through both lists until one is exhausted.
        while list1 and list2:
            # Compare the current values of list1 and list2.
            if list1.val < list2.val:
                # If list1's value is smaller, add list1's node to the merged list.
                node.next = list1
                # Move the pointer forward in list1.
                list1 = list1.next
            else:
                # If list2's value is smaller or equal, add list2's node to the merged list.
                node.next = list2
                # Move the pointer forward in list2.
                list2 = list2.next
            # Move the 'node' pointer forward to the newly added node.
            node = node.next

        # If one of the lists is not empty, append the remaining nodes to the merged list.
        # This works because the remaining nodes are already sorted.
        node.next = list1 or list2

        # Return the merged list, starting from the node after the dummy.
        return dummy.next


        