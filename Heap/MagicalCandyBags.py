# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=513590792640579&c=370634718267911&ppid=454615229006519&practice_plan=0
from heapq import heapify, heappop, heappush
def maxCandies(arr, k):
  # Write your code here
  heap = [-a for a in arr]
  heapify(heap)
  res = 0 #14
  for i in range(k): #0, 1,2 
    candies = -1*heappop(heap) #-7, -4, -3
    res += candies
    heappush(heap, -(candies//2)) #-3, -2
  return res