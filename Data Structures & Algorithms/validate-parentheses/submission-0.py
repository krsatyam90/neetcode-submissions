class Solution:
    def isValid(self, s: str) -> bool:
        #0(n)
        Map= {")" : "(","]" : "[" ,"}" : "{" }  #{Keys: values}
        stk = []    #LIFO

        for c in s:
            if c not in Map:
                stk.append(c)   #if it is an open bracket
            else:   #closing bracket
                if not stk:    #stk is empty
                    return False
                else:
                    popped = stk.pop()
                    if popped != Map[c]:
                        return False
                    
                    
        return not stk 

                    


                   







         
        