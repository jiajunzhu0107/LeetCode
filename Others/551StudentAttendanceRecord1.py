# https://leetcode.com/problems/student-attendance-record-i/
# 551. Student Attendance Record I
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_days = 0
        consecutive_late_days = 0
        for record in s:
            if record == 'A':
                absent_days += 1
                consecutive_late_days = 0
                if absent_days >= 2:
                    return False
            elif record == 'P':
                consecutive_late_days = 0
            else: # record == 'L'
                consecutive_late_days += 1
                if consecutive_late_days >= 3:
                    return False
            
        return True
            