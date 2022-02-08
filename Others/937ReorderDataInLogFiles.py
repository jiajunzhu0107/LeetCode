# https://leetcode.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            ident, content = log.split(' ',1)
            if content[0].isalpha():
                letter_logs.append((content,ident))
            else:
                digit_logs.append((content,ident))
        letter_logs.sort()
        letter_res = [' '.join([ident,content]) for content,ident in letter_logs]
        digit_res = [' '.join([ident,content]) for content,ident in digit_logs]
        return letter_res + digit_res