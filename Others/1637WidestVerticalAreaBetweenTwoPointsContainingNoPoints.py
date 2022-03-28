# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
# https://algo.monster/problems/widest_path_without_trees
def widest_path(x: List[int], y: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    x.sort()
    res = 0
    for i in range(1,len(x)):
        res = max(res, x[i]-x[i-1])
    return res


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [p[0] for p in points]
        sorted_x = sorted(x)
        res = 0
        for i in range(1,len(sorted_x)):
            res = max(res, sorted_x[i] - sorted_x[i-1])
        return res