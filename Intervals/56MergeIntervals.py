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

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        output = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if start <= prev_end:
                prev_end = max(end, prev_end)
            else:
                output.append([prev_start, prev_end])
                prev_start = start
                prev_end = end
        if output == [] or output[-1][0] != prev_start:
            output.append([prev_start, prev_end])
        return output
