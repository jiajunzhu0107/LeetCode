from typing import List
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475922559&idx=1&sn=77426b06f94e712acba06df275cde853&chksm=ff22f3f2c8557ae4fa6104b346e55d46974f635cb9b58a846125f5dd8644eaad53adfba40d6b&token=1145569493&lang=zh_CN#rd
# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        sum_window = 0
        res = 0
        while right < len(nums):
            if sum(nums[left:right+1]) < target:
                right += 1
            else:
                if left >= right:
                    res = 1
                    return res
                else:
                    if res != 0:
                        res = min(right + 1 - left,res)
                    else:
                        res = right + 1 - left
                    left += 1
        return res

if __name__ == '__main__':
    obj = Solution()
    nums = []
    target = 0
    obj.minSubArrayLen(target,nums)
    print(None == None)
    # i = 0
    # while i < 5:
    #     print(i)
    #     i += 1
        