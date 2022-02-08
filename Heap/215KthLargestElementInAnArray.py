# https://leetcode.com/problems/kth-largest-element-in-an-array/
from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(len(nums) - k + 1):
            a = heappop(nums)
            print(a)
        return a
            