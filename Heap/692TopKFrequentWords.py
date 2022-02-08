# https://leetcode.com/problems/top-k-frequent-words/
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        cnt = [(-val,key) for key,val in cnt.items()]
        heapify(cnt)
        res = []
        for _ in range(k):
            freq,word = heappop(cnt)
            res.append((freq,word))
        res.sort()
        res = [word for _,word in res]
        return res