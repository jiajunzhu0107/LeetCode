# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        if len(nums) == 1:
            return [nums[0]]
        
        res = []
        queue = []
        
        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                queue.pop(0)
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            
            if i >= k-1:
                res.append(nums[queue[0]])
        return res