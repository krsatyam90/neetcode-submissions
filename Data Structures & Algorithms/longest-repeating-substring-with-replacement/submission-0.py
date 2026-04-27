class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hashmap
        res = 0 # result
        l = 0 # left pointer
        maxf = 0    # maximum freq of the char

        for r in range (len(s)):
            count [s[r]] = 1 + count.get (s[r] , 0) # using .get to overcome from keyerror.
            maxf = max(maxf,count[s[r]])

            while (r-l+1) - maxf > k:
                count [s[l]] -= 1
                l +=1
            res = max(res, r-l+1)
        return res


        ## at O(n)




        