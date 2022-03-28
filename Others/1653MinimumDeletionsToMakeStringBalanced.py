# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/submissions/
class Solution:
    def minimumDeletions(self, s: str) -> int:
        charX = 'a'
        numY = 0
        minDel = 0
        for i in range(0, len(s)):
          if (charX == s[i]):
              minDel = min(numY, minDel + 1)
          else:
              numY = numY + 1
        return minDel
        