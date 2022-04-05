# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# https://algo.monster/problems/count_of_smaller_numbers_after_self

from itertools import count
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_lst = [0] * n    

        def mergeSort(index_list):
            # a=a+1
            # print(a)
            # count_lst[0]+=1
            # print(count_lst)
            if len(index_list) <= 1:
                return index_list
            mid = (0 + len(index_list) - 1)//2
            left = mergeSort(index_list[:mid+1])
            right = mergeSort(index_list[mid+1:])
            l = 0
            r = 0
            sortedList = []
            while l < len(left) or r < len(right):
                if r >= len(right) or (l < len(left) and nums[left[l]] <= nums[right[r]]):
                    sortedList.append(left[l])
                    count_lst[left[l]] += r
                    l += 1
                else:
                    sortedList.append(right[r])
                    r += 1

            return sortedList

        sorted_list = mergeSort([i for i in range(len(nums))])
        return count_lst



obj = Solution()
nums = [5,2,4,1]
obj.countSmaller(nums)