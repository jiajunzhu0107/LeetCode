# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/171/
class Solution:
    def myAtoi(self, s: str) -> int:
        s1 = s.lstrip(' ')
        if len(s1) <= 0:
            return 0
        if s1[0] in ['-', '+']:
            sign = s1[0]
            s1 = s1[1:]
        elif s[0].isnumeric():
            sign = '+'
        else:
            return 0
        num_str = ''
        index = 0
        print(s1[0])
        while (s1[index].isnumeric()) and (index < len(s1)):
            num_str += s1[index]
            index += 1
        if len(num_str) <= 0:
            return 0
        else:
            return int(sign + num_str)

s = '42'
print('a'+'b')
obj = Solution()
res = obj.myAtoi(s)
print(f'{res!r}')