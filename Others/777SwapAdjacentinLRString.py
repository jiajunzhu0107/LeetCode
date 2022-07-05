# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# 777. Swap Adjacent in LR String
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if start.replace("X", "") != end.replace("X", ""):
            return False
        index_l_start = [index for index, ch in enumerate(start) if ch == "L"]
        index_r_start = [index for index, ch in enumerate(start) if ch == "R"]
        index_l_end = [index for index, ch in enumerate(end) if ch == "L"]
        index_r_end = [index for index, ch in enumerate(end) if ch == "R"]
        
        for i in range(len(index_l_start)):
            if index_l_start[i] < index_l_end[i]:
                return False
        
        for i in range(len(index_r_start)):
            if index_r_start[i] > index_r_end[i]:
                return False
        
        return True