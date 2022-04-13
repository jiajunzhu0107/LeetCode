# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        def kSum(nums, target, k): #[-2,-1,0,0,1,2], 0, 4
            if k == 2:		#-1,0,0,1,2, 2, 3

                return twoSum(nums, target)
            res = set()
            for i in range(len(nums)): 
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                # print(i)
                res_i = kSum(nums[i+1:], target - nums[i], k-1) #[1,2]
                # print(f'{k}sum, target = {target - nums[i]}, nums = {nums[i+1:]}, {res_i}')
                for r in res_i:
                    
                    res.add((*r,nums[i]))
                # print(res)
            return res
        def twoSum(nums, target): #[0,0,1,2], 3
                        #[2,2,2,2], 4
            parsed = set() #[0,0,1,2]
            res = set()  #[1,2]
            for n in nums:
                if (target - n) in parsed:
                    res.add((target-n, n))
                parsed.add(n)
            return res
        nums.sort() #nums = [1,0,-1,0,-2,2], target = 0
        # print(nums, target)

        return kSum(nums, target, 4)
