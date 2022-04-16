# https://leetcode.com/problems/top-k-frequent-words/
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = [ (-val,key) for key, val in cnt.items() ]
        heapify(heap)
        res = []
        for i in range(k):
            _, word = heappop(heap)
            res.append(word)
        return res