class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def generate_parentheses(openCount, closeCount):

            if openCount == closeCount == n:
                res.append(''.join(stack))
                return
            if openCount < n:
                stack.append('(')
                generate_parentheses(openCount + 1, closeCount)
                stack.pop()
            if closeCount < openCount:
                stack.append(')')
                generate_parentheses(openCount, closeCount + 1)
                stack.pop()
        
        generate_parentheses(0,0)
        return res




        