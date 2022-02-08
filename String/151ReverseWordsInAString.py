# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def removeSpaces(self, s):
        left = 0
        right = len(s) - 1
        while left < right and s[left] == ' ':
            left += 1
        while left < right and s[right] == ' ':
            right -= 1
        
        new_s = []
        while left <= right:
            if s[left] != ' ':
                new_s.append(s[left])
            elif s[left] == ' ' and s[left-1] != ' ':
                new_s.append(s[left])
            left += 1
        return new_s
    
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
    
    def reverseWords(self, s: str) -> str:
        s = self.removeSpaces(s)
        s = self.reverseString(s)
        
        left = 0
        right = 0
        
        while left < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            s[left:right] = self.reverseString(s[left:right])
            left = right + 1
            right += 1
        return ''.join(s)
                