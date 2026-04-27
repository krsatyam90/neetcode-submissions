# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
     # Initialize the result to store the maximum diameter
        res = 0

    # Define a helper function for depth-first search (DFS) to calculate height and update diameter
        def dfs(root):
            nonlocal res  # Use the nonlocal keyword to modify the outer `res` variable
            # If the current node is null, its height is 0
            if not root:
                return 0
    
            # Recursively calculate the height of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)
    
            # Update the result with the maximum diameter seen so far
            # Diameter at the current node is the sum of the heights of left and right subtrees
            res = max(res, left + right)
    
            # Return the height of the current node (1 + maximum of left or right subtree height)
            return 1 + max(left, right)

        # Call the DFS function starting with the root of the tree
        dfs(root)

        # Return the final result, which is the maximum diameter of the tree
        return res

      