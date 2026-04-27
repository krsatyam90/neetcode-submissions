class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # return Counter(s) == Counter(t) # it is a datastucture in hashmap but it counts things automatically.
        # if len(s) != len(t):
        #     return False

        # CountS , CountT = {} , {} #  creating two empty set for the two set of Str,
        # for i in range (len(s)): # checking all the letter which are with in the Lenght of str S
        #     CountS [s[i]] = 1+CountS.get(s[i], 0) # The line of code is counting the occurrences of each element in the sequence s. If the element s[i] has been encountered before, its count is incremented by 1. If it is the first time the element has been encountered, it initializes its count to 1.

        #     CountT [t[i]] = 1+CountT.get(t[i], 0) # The get method of a dict (like for example characters) works just like indexing the dict, except that, if the key is missing, instead of raising a KeyError it returns the default value (if you call .get with just one argument, the key, the default value is None). 
        
        # return CountS == CountT


        # if len(s) != len(t):
        #     return False

        # CountS , CountT = {} , {}
        # for i in range (len(s)):
        #     CountS [s[i]] = 1 +CountS.get(s[i],0)
        #     CountT [t[i]] = 1 +CountT.get(t[i],0)

        # return CountS ==CountT

        if len(s)!= len(t):
            return False
        CountS, CountT = {},{}
        for i in range (len(s)):
            CountS[s[i]]= 1+CountS.get(s[i],0)
            CountT[t[i]]= 1+CountT.get(t[i],0)
        return CountS == CountT



