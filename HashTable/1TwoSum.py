# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #solution 1
        # parsed = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in parsed:
        #         return [parsed[complement],i]
        #     parsed[nums[i]] = i
        
        #solution2
        parsed = {}
        for index, num in enumerate(nums):
            if target - num in parsed:
                return [parsed[target-num],index]
            parsed[num] = index
        return []