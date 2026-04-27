class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: if t is empty, return an empty string 
        if t == "":
            return ""
        
        # Initialize freq count for chara in t 
        countT, window = {},{}  #hashmap

        #fill countT with freq of chara in t
        for c in t :
            countT[c] = 1 + countT.get(c, 0)

        have , need = 0 ,len(countT)
        res, reslen = [-1,-1], float("infinity")
        l =0
        # slide right pointer across s
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            #check if current character satisfies the frequency requirement in t 
            if c in countT and window[c] == countT[c]:
                have +=1
            #try to shrink the window when all characters are found 
            while have == need:
                if (r -l+1) < reslen:
                    res =[l,r]
                    reslen =r-l+1
                # shrink the window from the left 
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1

        #return the smallerst valid window or an empty string if none found
        l, r = res
        return s[l: r+1] if reslen != float("infinity") else""
        


        

        