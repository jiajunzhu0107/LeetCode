# https://leetcode.com/problems/minimum-time-difference/

from math import inf
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [0] * 60 * 24
        for timePoint in timePoints:
            time = timePoint.split(":")
            minute = int(time[0]) * 60 + int(time[1])
            if minutes[minute] == 1:
                return 0
            minutes[minute] = 1
        prev_minute = None
        first_minute = None
        output = inf
        for minute, val in enumerate(minutes):
            if val == 1:
                if prev_minute is None:
                    prev_minute = minute
                    first_minute = minute
                else:
                    output = min(output, minute - prev_minute)
                    prev_minute = minute
        output = min(output, 60 * 24 - prev_minute + first_minute)
        return output
        
                    
            