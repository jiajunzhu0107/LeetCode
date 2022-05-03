# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        first_row = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    first_row = r
                    break
            if first_row is not None:
                break
        if first_row is None:
            return True
        #flip first_row

        grid[first_row] = [0 if i == 1 else 1 for i in grid[first_row]]
        flip_cols = set()
        for idx, c in enumerate(grid[first_row]):
            if c == 1:
                flip_cols.add(idx)
        
        for r in range(rows):
            for c in range(cols):
                if c in flip_cols:
                    grid[r][c] = 0 if grid[r][c] == 1 else 1
                    
        for r in range(rows):
            if grid[r] != [1]*cols and grid[r] != [0]*cols:
                return False
        return True