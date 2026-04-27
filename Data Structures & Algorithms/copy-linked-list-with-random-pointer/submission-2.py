#class Node:
 #   def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
  #      self.val = int(x)
   #     self.next = next
    #    self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a linked list where each node has a 'next' pointer and a 'random' pointer.
        
        :param head: The head of the original linked list.
        :return: The head of the deep-copied linked list.
        """
        # A dictionary to map original nodes to their copies, with None mapped to None for edge cases
        oldtocopy = {None: None}
        
        # First pass: Create copies of each node and store them in the dictionary
        cur = head  # Start with the head of the original list
        while cur:
            copy = Node(cur.val)  # Create a copy of the current node with the same value
            oldtocopy[cur] = copy  # Map the original node to its copy
            cur = cur.next  # Move to the next node in the original list

        # Second pass: Set the 'next' and 'random' pointers for each copied node
        cur = head  # Reset cur to the head of the original list
        while cur:
            copy = oldtocopy[cur]  # Get the copied node corresponding to the original node
            copy.next = oldtocopy[cur.next]  # Set the 'next' pointer for the copied node
            copy.random = oldtocopy[cur.random]  # Set the 'random' pointer for the copied node
            cur = cur.next  # Move to the next node in the original list
        
        # Return the head of the copied list, which corresponds to the copy of the original head
        return oldtocopy[head]
        
        

        