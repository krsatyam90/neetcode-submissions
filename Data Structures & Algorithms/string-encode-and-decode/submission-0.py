from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            # Find the position of the next '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Move the index to the start of the string
            i = j + 1
            
            # Extract the string
            res.append(s[i:i + length])
            
            # Move the index to the end of the current string
            i += length
        
        return res