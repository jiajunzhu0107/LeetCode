# https://leetcode.com/problems/maximum-average-pass-ratio/
from heapq import heapify, heappop, heappush
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #max heap
        ratings = [(p/n - (p+1)/(n+1), p, n) for p,n in classes]
        heapify(ratings)
        for _ in range(extraStudents):
            (r,p,n) = heappop(ratings)
            heappush(ratings, ((p+1)/(n+1) - (p+2)/(n+2), p+1, n+1))
        res = sum([p/n for r,p,n in ratings])/len(classes)
        return res

a = [1,2,3]
b = a
a.append(4)
a = a[:1]
print(a)
print(b)