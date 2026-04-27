class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 , n2 = len(s1), len(s2)

        if n1 > n2 :
            return False
        
        s1counts = [0]* 26
        s2counts = [0]* 26

        for i in range (n1):
            s1counts[ord(s1[i]) - 97 ]  += 1
            s2counts[ord(s2[i]) - 97 ]  += 1
            
        if s1counts == s2counts:
            return True

        for i in range (n1,n2):
            s2counts[ord(s2[i]) - 97 ]  += 1
            s2counts[ord(s2[i-n1]) - 97 ]  -= 1
            if s1counts == s2counts:
                return True
        return False





        


        