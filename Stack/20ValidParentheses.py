# https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for i in s:
            if i not in pairs:
                stack.append(i)
            elif len(stack) <= 0 or pairs[i] != stack.pop():
                return False
        
        return not stack