class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'

        def compute(x, y, operator):
            if operator == "+":
                return x + y
            elif operator == "*":
                return x * y
            elif operator == "-":
                return x - y
            elif operator == "/":  # Changed to correct order and ensure integer division
                if y == 0:
                    raise ValueError("Division by zero.")
                return int(x / y)

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right = stack.pop()  # the right operand
                left = stack.pop()  # the left operand
                result = compute(left, right, token)
                stack.append(result)

        return stack.pop()  # Return the last item in the stack, which is the result

