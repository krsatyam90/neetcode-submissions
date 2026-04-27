class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = [1]*len(nums)

        # right = [1]*len(nums)

        # for i in range (1,len(nums)):
        #     left [i] = left[i-1] * nums[i-1]
        # for i in range (len(nums) -2,-1,-1):
        #     right [i] = right[i+1] * nums[i+1]
        # ans = [0] *len(nums)
        # for i in range (len(nums)):
        #     ans[i] =left[i] * right[i]
        
        # return ans
        res = [1]*(len(nums))
        for i in range (1,len(nums)):
            res [i] = res[i-1] * nums[i-1]
            postfix = 1
        for i in range (len(nums) -1, -1, -1):
            res [i]*= postfix
            postfix *=nums[i]
        return res
        # res = [1]*(len(nums)) # initalize the result list with 1s
        # #Calculate prefix products
        # for i in range (1, len(nums)):
        #     res [i] = res[i-1]*nums[i-1]
        # # Initialize postfix to 1
        #     postfix = 1
        # # Calculate postfix products and multiply with prefix products in res
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res