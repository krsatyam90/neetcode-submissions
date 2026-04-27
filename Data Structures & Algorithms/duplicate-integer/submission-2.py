class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset = set ()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        # hashmap =set ()
        # for n in nums:
        #     if n in hashmap:
        #         return True
        #     hashmap.add(n)
        # return False  
        hashset = set ()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False    