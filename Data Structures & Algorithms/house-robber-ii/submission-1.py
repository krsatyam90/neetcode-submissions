class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.alt_rob(nums[1:]),
                            self.alt_rob(nums[:-1]))
    def alt_rob(self,nums):
        rob1, rob2 = 0,0 
        for n in nums:
            rob = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = rob
        return rob2

        