#https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/solution/

from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        target = (rows - 1, cols - 1)
        
        if k >= rows + cols - 2:
            return rows+ cols - 2
        
        queue = deque([(0,(0,0,k))])
        visited = {(0,0,k)}
        
        while queue:
            path, (node_r, node_c, quota) = queue.popleft()
            if (node_r, node_c) == target:
                return path
            for child_r, child_c in [(node_r - 1, node_c), (node_r+1,node_c), (node_r, node_c+1), (node_r,node_c-1)]:
                if (0 <= child_r < rows) and (0 <= child_c < cols) :
                    remain_quota = quota - grid[child_r][child_c]
                    if remain_quota >= 0 and (child_r,child_c,remain_quota) not in visited:
                        queue.append((path + 1,(child_r,child_c,remain_quota)))
                        visited.add((child_r,child_c,remain_quota))

        return -1

#A*
# from collections import deque
from heapq import heappush, heappop
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        target = (rows - 1, cols - 1)
        
        def manhattan_dist(row,col):
            return rows-row-1 + cols-col-1
        
        if k >= rows + cols - 2:
            return rows+ cols - 2
        
        # queue = deque([(0,(0,0,k))])
        queue = [(rows+cols-2,0,(0,0,k))]
        visited = {(0,0,k)}
        
        while queue:
            # path, (node_r, node_c, quota) = queue.popleft()
            est_total, path, (node_r, node_c, quota) = heappop(queue)
            if (node_r, node_c) == target:
                return path
            for child_r, child_c in [(node_r - 1, node_c), (node_r+1,node_c), (node_r, node_c+1), (node_r,node_c-1)]:
                if (0 <= child_r < rows) and (0 <= child_c < cols) :
                    remain_quota = quota - grid[child_r][child_c]
                    if remain_quota >= 0 and (child_r,child_c,remain_quota) not in visited:
                        # queue.append((path + 1,(child_r,child_c,remain_quota)))
                        heappush(queue, (manhattan_dist(child_r,child_c)+path+1 ,path + 1,(child_r,child_c,remain_quota)))
                        visited.add((child_r,child_c,remain_quota))

        return -1
