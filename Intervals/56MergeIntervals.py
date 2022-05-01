# https://leetcode.com/problems/merge-intervals/
# https://algo.monster/problems/merge_intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        if len(intervals) < 2:
            return intervals

        curr_int = intervals[0] #[1,6]
        for i in range(1, len(intervals)):
            if curr_int[1] >= intervals[i][0]:
                curr_int[1] = max(curr_int[1], intervals[i][1])
            else:
                res.append(curr_int)
                curr_int = intervals[i]
        res.append(curr_int)

        return res
