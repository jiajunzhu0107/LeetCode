# https://leetcode.com/problems/k-closest-points-to-origin/
from heapq import heapify, heappop
from typing import List

from sqlalchemy import desc
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #min_heap
        distances = [(math.sqrt(x**2 + y**2),x,y) for x,y in points]
        heapify(distances)
        res = []
        for _ in range(k):
            _,x,y = heappop(distances)
            res.append([x,y])
        return res

a = (1,'abc')
b = (1,'baa')
c = (2,'aaa')
list1 = [b,c,a]
list1.sort(reverse = True)
print(list1)