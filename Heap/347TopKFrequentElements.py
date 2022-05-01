# https://leetcode.com/problems/top-k-frequent-elements/
# quick select O(N)
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = [(-1*freq,n) for n,freq in cnt.items()]
        heapify(heap)
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res