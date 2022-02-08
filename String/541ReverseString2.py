# https://leetcode.com/problems/reverse-string-ii/
class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        
        for i in range(0,len(s),2*k):
            res[i:i+k] = self.reverseString(res[i:i+k])
        return ''.join(res)