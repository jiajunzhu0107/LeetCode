# https://leetcode.com/problems/daily-temperatures/
# https://algo.monster/problems/daily_temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]# [1,1,4,2,1,1,0,0]
        stack = []
        for idx, t, in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < t:
                popped_idx = stack.pop()
                res[popped_idx] = idx-popped_idx
            stack.append(idx)
        return res