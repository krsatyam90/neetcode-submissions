class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Only add open parathesis if Open < n
        #only add a closing parathesis if closed < open 
        #valid IFF open == closed == n

        stack = []
        res =[]

        def backtraking(OpenN,CloseN):
            if OpenN == CloseN == n:
                res.append("".join (stack))
                return 
            if OpenN < n:
                stack.append("(")
                backtraking(OpenN +1, CloseN)
                stack.pop()
            if CloseN < OpenN:
                stack.append(")")
                backtraking(OpenN,CloseN +1)
                stack.pop()

        backtraking(0,0)
        return res
        