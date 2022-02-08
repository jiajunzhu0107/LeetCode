# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            complement = curr - k
            if complement in prefixSum:
                res += prefixSum[complement]
            if curr not in prefixSum:
                prefixSum[curr] = 1
            else:
                prefixSum[curr] += 1
        return res
        