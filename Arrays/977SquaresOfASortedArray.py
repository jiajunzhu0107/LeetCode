from typing import List
# https://leetcode.com/problems/squares-of-a-sorted-array/
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475922258&idx=1&sn=95bfe3da6211191d5335cb520820bc99&chksm=ff22f4dfc8557dc9eca2d93ed8b28e4e01c8557ed7e239b6b0265ac7d13ea50d44ab310637c2&token=1145569493&lang=zh_CN#rd
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [-1] * len(nums)
        pos = len(nums) - 1
        while pos >= 0:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                res[pos] = nums[right] * nums[right]
                right -= 1
            else:
                res[pos] = nums[left] * nums[left]
                left += 1
            pos -= 1
        return res