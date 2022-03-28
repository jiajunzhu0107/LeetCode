# https://leetcode.com/problems/longest-happy-string/
from heapq import heapify, heappop, heappush
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heappush(heap, (-a,'a'))
        if b > 0:
            heappush(heap, (-b,'b'))
        if c > 0:
            heappush(heap, (-c,'c'))
        prev_val = ''
        cool_down = None
        res = ''
        while heap:
            cnt, val = heappop(heap)
            res += val
            cnt += 1
            
            if prev_val == val:
                if cnt < 0:
                    cool_down = (cnt,val)
            else:
                if cool_down is not None:
                    heappush(heap, cool_down)
                    cool_down = None
                if cnt < 0:
                    heappush(heap, (cnt, val))
            prev_val = val
        return res