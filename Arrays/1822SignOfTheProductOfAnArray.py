# https://leetcode.com/problems/sign-of-the-product-of-an-array/
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_cnt = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                neg_cnt += 1
        if neg_cnt % 2 == 0:
            return 1
        else:
            return -1