# https://algo.monster/problems/min_steps_to_make_piles_equal_height
from typing import List, Counter

def min_steps(nums: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    cnt = Counter(nums)
    nums = sorted(cnt.keys())
    res = 0
    for i in range(len(nums)-1,-1,-1):
        res += i *cnt[nums[i]]
    
    return res