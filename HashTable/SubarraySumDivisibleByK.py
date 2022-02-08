# https://algo.monster/problems/subarray_sum_divisible
from typing import Counter, List

def subarray_sum_divisible(nums: List[int], k: int) -> int:
    remainders = Counter({0: 1})
    cur_sum = 0
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        cur_sum += num
        remainder = cur_sum % k
        complement = (k - remainder) % k
        if complement in remainders:
            count += remainders[complement]
        remainders[complement] += 1

    return count

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_divisible(nums, k)
    print(res)