class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        txn = '+-*/'
        sol = 0

        def compute(y, x, tx):
            if tx == "+":
                return x + y
            elif tx == "*":
               return x * y
            elif tx == "-":
                return x - y
            else:
                return int(float(x) / y)

        for tx in tokens:
            if tx not in txn:
                stack.append(int(tx))
            else:
                right_val = stack.pop()
                left_val = stack.pop()
                sol = compute(right_val, left_val, tx)
                stack.append(sol)
        return stack.pop()