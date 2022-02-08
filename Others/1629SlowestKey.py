# https://leetcode.com/problems/slowest-key/
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        largestKey = 'a'
        longestTime = 0
        for i in range(len(releaseTimes)):
            if i == 0:
                duration = releaseTimes[i]
            else:
                duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > longestTime:
                longestTime = duration
                largestKey = keysPressed[i]
            elif duration == longestTime:
                if keysPressed[i] > largestKey:
                    largestKey = keysPressed[i]
        return largestKey