# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        @cache
        def fn(i,d):
            if d == 1:
                return max(jobDifficulty[i:])
            n = len(jobDifficulty)
            res = inf
            todayDifficulty = 0
            for j in range(i, n - d + 1):
                todayDifficulty = max(todayDifficulty,jobDifficulty[j])
                res = min(res, todayDifficulty + fn(j+1,d-1))
            return res
        return fn(0,d)