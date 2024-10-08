
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        for token in tokens:
            if token not in operators:  
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                else:  
                    stack.append(int(b / a))
        
        return stack.pop()
