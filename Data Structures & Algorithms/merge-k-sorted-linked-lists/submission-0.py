# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # If the list is empty, return None
            return None 

        # Continue merging lists until only one list remains
        while len(lists) > 1:
            merged_lists = []  # Temporary list to store merged pairs of lists
            # Iterate through the lists two at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list in the pair
                l2 = lists[i + 1] if i + 1 < len(lists) else None  # Second list in the pair (if it exists)
                # Merge the two lists and add the result to merged_lists
                merged_lists.append(self.mergeList(l1, l2))
            # Update lists to the newly merged lists
            lists = merged_lists
        
        # The final merged list is the only remaining list
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()  # Create a dummy node
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append the remaining nodes of l1 or l2
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next



        