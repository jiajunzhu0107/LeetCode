# https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            letters = ''
            closed = False
            nums = ''
            was_num = False
            if c == ']':
                #no need to validate stack status
                while stack:
                    s = stack.pop()
                    if s.isalpha():
                        if was_num:
                            l = int(nums)*letters
                            stack.append(s+l)
                            nums = ''
                            letters = ''
                            closed = False
                            break
                        else:
                            letters = s + letters
                        was_num = False
                    elif s == '[':
                        closed = True
                        if was_num:
                            l = int(nums)*letters
                            stack.append(l)
                            nums = ''
                            letters = ''
                            closed = False
                            break
                        was_num = False
                    elif s.isnumeric():
                        was_num = True
                        nums = s + nums
                if nums != '':
                    stack.append(int(nums)*letters)
                    nums = ''
                    letters = ''
                    closed = False
            else:
                stack.append(c)
        res = ''
        while stack:
            res = stack.pop()+res
        return res
