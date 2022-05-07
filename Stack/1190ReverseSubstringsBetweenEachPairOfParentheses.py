# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c in {')','}',']'}:
                words = []
                while stack:
                    curr_c = stack.pop()
                    if curr_c in {'(','[','{'}:
                        for i in words:
                            stack.append(i)
                        break
                    else:
                        words.append(curr_c)
            else:
                stack.append(c)
        
        return ''.join(stack)