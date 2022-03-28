# https://leetcode.com/problems/largest-divisible-subset/
# https://algo.monster/problems/largest_divisible_subset
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dic = {
            ind:[nums[ind]] for ind in range(len(nums))
        }
        max_len = 1
        res = dic[0]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dic[i]) < len(dic[j]) + 1:
                        dic[i] = dic[j] + [nums[i]]
                        if len(dic[i]) > max_len:
                            max_len = len(dic[i])
                            res = dic[i]
        return res