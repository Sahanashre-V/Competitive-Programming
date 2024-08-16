class Solution:    
    def InfixtoPostfix(self, exp):
        s = len(exp)
        i = 0
        result = ""
        stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
        
        while i < s:
            if (exp[i] >= 'A' and exp[i] <= 'Z') or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
                result += exp[i]
            elif exp[i] == '(':
                stack.append(exp[i])
            elif exp[i] == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()  
            else:
                while stack and stack[-1] != '(' and precedence[exp[i]] <= precedence[stack[-1]]:
                    result += stack.pop()
                stack.append(exp[i])
            
            i += 1
    
        while stack:
            result += stack.pop()
        
        return result

