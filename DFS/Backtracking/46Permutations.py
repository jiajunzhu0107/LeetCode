# https://leetcode.com/problems/permutations/
# https://algo.monster/problems/permutations
from sklearn.utils import resample


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(used,path, res):
            if len(path) == len(nums):
                p = copy.deepcopy(path)
                res.append(p)
                return
            
            for c in nums:
                if not used[c]:
                    path.append(c)
                    used[c] = True
                    dfs(used, path, res)
                    path.pop()
                    used[c] = False
        
        used = {c:False for c in nums}
        path = []
        res = []
        dfs(used,path,res)
        return res