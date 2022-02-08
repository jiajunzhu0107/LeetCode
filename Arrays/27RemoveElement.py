from typing import List
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475922234&idx=1&sn=5f0a3fce40927c80ff5608da90b6fcd0&chksm=ff22f4b7c8557da10186decdfd4b1f57277b44e1f452388be2ef407bd5e91f8b2e24c624fceb&token=1145569493&lang=zh_CN#rd
# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == '__main__':
    obj = Solution()
    nums = []
    val = 0
    obj.removeElement(nums,val)