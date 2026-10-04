class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                x, y = stack.pop(), stack.pop()
                if i == '*':
                    stack.append(x*y)
                elif i == '+':
                    stack.append(x+y)
                elif i == '/':
                    stack.append(int(y/x))
                else:
                    stack.append(y-x)
        return stack.pop()