# https://leetcode.com/problems/race-car/submissions/
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        while queue: #queue = [ [15,16],[7,1],[6,-2],[3,-1],[1,-1],[-1,-2],[0,1]] ] 
            pos, speed, moves = queue.popleft() #0, 1
            if pos == target:
                return moves
            for ins in ['A', 'R']:
                if ins == 'A':
                    new_pos = pos + speed
                    new_speed = speed * 2
                else: # ins == 'R'
                    new_pos = pos
                    new_speed = -1 if speed > 0 else 1
                if new_pos >= 0 :
                    queue.append((new_pos, new_speed, moves + 1))

#optimized
class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(0,1,0)])
        while queue: #queue = [ [15,16],[7,1],[6,-2],[3,-1],[1,-1],[-1,-2],[0,1]] ] 
            pos, speed, moves = queue.popleft() #0, 1
            if pos == target:
                return moves
            new_pos = pos + speed
            new_speed = speed * 2
            queue.append((new_pos, new_speed, moves + 1))
            if (new_pos > target and speed > 0) or (new_pos < target and speed < 0 ):
                new_speed = -1 if speed > 0 else 1
                queue.append((pos, new_speed, moves + 1))