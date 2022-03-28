# https://leetcode.com/problems/partition-equal-subset-sum/


#this will time out
class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        used = [False for i in range(len(nums))]
        @lru_cache
        def dfs(cur_sum):
            # print(cur_sum, i, used)
            if cur_sum == target:
                # print(cur_sum, nums[i])
                return True
            else:
                
                for i in range(len(nums)):
                    if not used[i]:
                        used[i] = True
                        if dfs(cur_sum + nums[i]):
                            return True
                        used[i] = False
            return False
        return dfs(0)