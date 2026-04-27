class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashmap = {}
        for i ,n in enumerate(nums):
            diff = target - n
            if diff in Hashmap:
                return [Hashmap[diff], i]
            Hashmap[n]=i
        return 
 