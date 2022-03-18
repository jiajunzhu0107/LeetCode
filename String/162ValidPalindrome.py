# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/162/
from sympy import false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join([c.lower() for c in s if c.isalnum() ])
        print(s1)
        head = 0
        tail = len(s1) - 1
        while(head < tail):
            if s1[head] != s1[tail]:
                return False
            head += 1
            tail -= 1
        return True

obj = Solution()
s = 'A man, a plan, a canal: Panama'
res = obj.isPalindrome(s)
print(res)