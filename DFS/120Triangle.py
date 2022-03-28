# https://leetcode.com/problems/triangle/
# https://algo.monster/problems/triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(row,col):
            if row + 1 >= len(triangle):
                return triangle[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            left = dfs(row+1,col)
            res = min(dfs(row+1,col),dfs(row+1,col+1)) + triangle[row][col]
            memo[(row,col)] = res
            return res
        
        return dfs(0,0)