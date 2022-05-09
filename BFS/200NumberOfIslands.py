# https://leetcode.com/problems/number-of-islands/
# Union Find/DSU also works
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) <= 0:
            return 0
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    queue = deque([(r,c)])
                    res += 1
                    while queue:
                        node_r, node_c = queue.popleft()
                        for child_r, child_c in [(node_r+1,node_c),(node_r-1,node_c),(node_r,node_c+1),(node_r,node_c-1)]:
                            if child_r >=0 and child_c >=0 and child_r <rows and child_c <cols and grid[child_r][child_c] == '1':
                                grid[child_r][child_c] = 0
                                queue.append((child_r,child_c))
                                    
        return res
                    