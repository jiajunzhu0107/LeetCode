# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        sum_grid = [[float('inf') for j in grid[0]] for i in grid]
        
        current_sum = 0
        for i in range(row):
            current_sum += grid[i][0]
            sum_grid[i][0] = current_sum
        
        current_sum = 0
        for i in range(col):
            current_sum += grid[0][i]   
            sum_grid[0][i] = current_sum
            
        for r in range(1, row):
            for c in range(1, col):
                sum_grid[r][c] = min(sum_grid[r-1][c], sum_grid[r][c-1]) + grid[r][c]
        return sum_grid[-1][-1]