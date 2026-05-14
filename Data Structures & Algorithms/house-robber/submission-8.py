class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #Base case 
        if n == 0:
            return 0 
        if n == 1:
            return nums[0]
        # process
        prev2 = nums[0]
        prev1 = max(nums[0],nums[1])
        
        #Space optimi
        for i in range(2,n):
            curr = max(prev1 , nums[i]+prev2)
            prev2 = prev1
            prev1 = curr
        return prev1

        