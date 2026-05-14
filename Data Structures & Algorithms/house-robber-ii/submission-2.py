class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.done(nums[1:]),self.done(nums[:-1]))
    def done(self,nums):
        h1,h2 = 0 , 0
        for num in nums:
            maxrob= max(h1+num,h2)
            h1 = h2
            h2 = maxrob
        return h2
        

        


        