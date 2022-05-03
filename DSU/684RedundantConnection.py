class DSU:
    def __init__(self): #3 <= n <= 1000
        self.parent = [i for i in range(1001)]
        self.rank = [0] * 1001
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # tree compression
        return self.parent[x]
    
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return False
        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[yp] = xp
            self.rank[xp] += 1
        return True

class Solution(object):
    
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for x, y in edges:
            if not dsu.union(x,y):
                return [x,y]