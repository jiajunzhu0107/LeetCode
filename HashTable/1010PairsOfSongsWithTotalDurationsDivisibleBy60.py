# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        parsed = {}
        res = 0
        for t in time:
            if (-t % 60) in parsed:
                res += parsed[-t % 60]
            if t % 60 in parsed:
                parsed[t % 60] += 1
            else:
                parsed[t%60] = 1
        return res