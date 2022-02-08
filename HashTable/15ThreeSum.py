# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        
        res = set()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            hash = {}
            for j in range(i+1,len(nums)):
                if nums[j] not in hash:
                    hash[-nums[i]-nums[j]] = 1
                else:
                    res.add((nums[i],-nums[i]-nums[j],nums[j]))
        return list(res)