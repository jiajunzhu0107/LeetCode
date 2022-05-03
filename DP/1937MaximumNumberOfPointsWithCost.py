# https://leetcode.com/problems/maximum-number-of-points-with-cost/
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        curr_row = points[0]
        # prev_row = copy.deepcopy(curr_row)
        for r in range(1,len(points)):
            # left -> right
            max_val = -inf
            for c in range(len(points[0])):
                max_val = max(max_val-1,curr_row[c])
                curr_row[c] = max_val
            #right -> left
            max_val = -inf
            for c in range(len(points[0])-1,-1,-1):
                max_val = max(max_val-1,curr_row[c])
                curr_row[c] = max_val
            
            #update
            for c in range(len(points[0])):
                curr_row[c] = curr_row[c] + points[r][c]
                # print(curr_row)
            
        return max(curr_row)