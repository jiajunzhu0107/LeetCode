
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
#not coded by myself
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # if not is_valid(s):
        #     return -1

        s = list(s)
        n = len(s)

        count = 0
        i = 0
        while i < n // 2:
            left = i
            right = n - left - 1

            while left < right:
                if s[left] == s[right]:
                    break
                else:
                    right -= 1

            if left == right:
                # s[left] is the character in the middle of the palindrome
                (s[left], s[left + 1]) = (s[left + 1], s[left])
                count += 1
            else:
                for j in range(right, n - left - 1):
                    (s[j], s[j + 1]) = (s[j + 1], s[j])
                    count += 1
                i += 1
        return count
