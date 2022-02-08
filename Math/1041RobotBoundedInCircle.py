# https://leetcode.com/problems/robot-bounded-in-circle/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        north = [0,1]
        east = [1,0]
        south = [0,-1]
        west = [-1,0]
        moves = [north,east,south,west]
        facing = 0
        x = 0
        y = 0
        for i in instructions:
            if i == 'L':
                facing = (facing + 3) % 4
            elif i == 'R':
                facing = (facing + 1) % 4
            else:
                x += moves[facing][0]
                y += moves[facing][1]
        
        if (x == 0 and y == 0) or (facing != 0):
            return True
        return False