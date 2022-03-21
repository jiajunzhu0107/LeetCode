# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/171/
class Solution:
    def myAtoi(self, s: str) -> int:
        s1 = s.lstrip(' ')
        if len(s1) <= 0:
            return 0
        if s1[0] in ['-', '+']:
            sign = s1[0]
            s1 = s1[1:]
        elif s1[0].isnumeric():
            sign = '+'
        else:
            return 0
        num_str = ''
        index = 0
        while index < len(s1) and s1[index].isnumeric() :
            num_str += s1[index]
            index += 1
        if len(num_str) <= 0:
            return 0
        else:
            if int(sign + num_str) < -2**31:
                return -2 ** 31
            elif int(sign + num_str) > 2**31 -1:
                return 2 **31 -1
            else:
                return int(sign + num_str)
a = -2 **31      
print(a)
s = '42'
obj = Solution()
res = obj.myAtoi(s)
print(f'{res!r}')