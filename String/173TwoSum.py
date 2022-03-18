# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/173/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, n in enumerate(nums):
            if n in dic:
                return index, dic[n]
            else:
                dic[target-n] = index
        return None

obj = Solution()
nums = [2,7,11,15]
target = 9
res = obj.twoSum(nums, target)
print(res)