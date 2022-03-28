# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 != 0:
            res.append(0)
            for i in range(1,(n//2)+1):
                res += [-i,i]
        else:
            for i in range(1,(n//2)+1):
                res += [-i,i]
        return res