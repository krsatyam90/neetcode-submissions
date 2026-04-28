class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsubarray = nums[0]
        curSum = 0 
        for n in nums:
            if curSum < 0:
                curSum = 0 
            curSum += n
            maxsubarray =max(maxsubarray,curSum)
        return maxsubarray
        