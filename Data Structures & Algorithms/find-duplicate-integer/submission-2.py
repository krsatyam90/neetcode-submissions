class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # slow , fast = 0, 0 
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast :
        #         break
        # slow2 = 0
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        #     if slow == slow2:
        #         return slow




        """
        Finds the duplicate number in an array where the numbers are in the range [1, n], 
        and there is only one duplicate number. This solution uses Floyd's Tortoise and Hare 
        (Cycle Detection) algorithm to find the duplicate in O(n) time and O(1) space.

        :param nums: List of integers containing n + 1 integers, where each integer is in the range [1, n].
        :return: The duplicate number.
        """
        # Initialize two pointers for the cycle detection
        slow, fast = 0, 0

        # Phase 1: Detect a cycle using the slow and fast pointer approach
        while True:
            slow = nums[slow]  # Move slow pointer by one step
            fast = nums[nums[fast]]  # Move fast pointer by two steps
            if slow == fast:  # Cycle detected
                break
        
        # Phase 2: Find the entrance to the cycle, which is the duplicate number
        slow2 = 0  # Start a new pointer from the beginning of the array
        while True:
            slow = nums[slow]  # Move the first pointer by one step
            slow2 = nums[slow2]  # Move the second pointer by one step
            if slow == slow2:  # When both pointers meet, we've found the duplicate
                return slow
 
        