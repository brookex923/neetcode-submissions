class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        res = 0
        for t in tokens:
            print(stack)
            if t not in ops:
                stack.append(int(t))
            
            if t == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            if t == "-":
                a,b = stack.pop(), stack.pop()
                res = b-a
                stack.append(res)
            if t == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            if t == "/":
                a, b = stack.pop(), stack.pop()
                res = int(float(b)/a)
                stack.append(res)
        
        return stack[0]