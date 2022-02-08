# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                if i == '+':
                    stack.append(left + right)
                elif i == '-':
                    stack.append(left - right)
                elif i == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            
        return stack[0]