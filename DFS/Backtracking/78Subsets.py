# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr_nums,i):
            res.append(curr_nums)
            if i >= len(nums):
                return
            for j in range(i+1,len(nums)):
                n = curr_nums + [nums[j]]
                # res.append(n)
                dfs(n,j)
        
        dfs([],-1)
        return res