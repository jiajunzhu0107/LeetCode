# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def isValid(target, m, nums):
            subarrays = 0
            curr_sum = 0
            for n in nums:
                if n > target:
                    return False
                curr_sum += n
                if curr_sum > target:
                    subarrays += 1
                    curr_sum = n
                    if subarrays > m:
                        return False
            subarrays += 1
            if subarrays > m:
                return False
            else:
                return True
            
        
        left = 0
        right = sum(nums)
        min_sum = None
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid, m, nums):
                min_sum = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_sum