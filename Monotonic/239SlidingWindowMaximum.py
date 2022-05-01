# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 0:
            return []
        res = [] #3, 3, 
        queue = deque([0]) #[3,-1, -3]
        for i in range(1,k):
            while len(queue) > 0 and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        for i in range(k,len(nums)):
            if queue[0] <= i-k:
                queue.popleft()

            while len(queue) > 0 and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            res.append(nums[queue[0]])
        return res