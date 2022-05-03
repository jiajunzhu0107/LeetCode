# https://leetcode.com/problems/detect-squares/
class DetectSquares:

    def __init__(self):
        #{x:{y:cnt}}
        self.nodes = {}

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        if x not in self.nodes:
            self.nodes[x] = {y:1}
        else:
            if y not in self.nodes[x]:
                self.nodes[x][y] = 1
            else:
                self.nodes[x][y] += 1
        # print(self.nodes)
    
    def count(self, point: List[int]) -> int:
        #get first possible node Xs
        x = point[0]
        y = point[1]
        if x not in self.nodes:
            return 0
        cnt = 0
        for first_y,count in self.nodes[x].items():
            dist = abs(y-first_y)
            if dist == 0:
                continue
            if x-dist in self.nodes:
                if y in self.nodes[x-dist] and first_y in self.nodes[x-dist]:
                    cnt += self.nodes[x-dist][y] * self.nodes[x-dist][first_y] * count
            if x+dist in self.nodes:
                if y in self.nodes[x+dist] and first_y in self.nodes[x+dist]:
                    cnt += self.nodes[x+dist][y] * self.nodes[x+dist][first_y] * count
        return cnt
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)