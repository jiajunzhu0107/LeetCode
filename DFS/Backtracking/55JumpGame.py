# https://leetcode.com/problems/jump-game/
# this backtracking will time out
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        deadends = [False] * len(nums)
        def backtracking(i):
            if i > (len(nums) - 1) or deadends[i] or i < 0:
                return False
            elif i == len(nums) - 1:
                return True
            else:
                for j in range(1, nums[i]+1):
                    if backtracking(i+j):
                        return True
                deadends[i] = True
                return False
        return backtracking(0)