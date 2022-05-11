# https://leetcode.com/problems/nested-list-weight-sum-ii/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from cmath import inf
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        nums = []
        depth = []
        self.maxDepth = 0
        
        def findNums(arr,currDepth):
            # print(arr)
            if arr.isInteger():
                nums.append(arr.getInteger())
                depth.append(currDepth)
                self.maxDepth = max(self.maxDepth, currDepth)
                return
            else:
                for i in arr.getList():
                    findNums(i,currDepth+1)
                    
        for i in nestedList:
            findNums(i,0)
        # res = sum([nums[i] * (maxDepth - depth[i] + 1) for i in range(len(nums))])
        res = 0
        for i in range(len(nums)):
            weight = self.maxDepth - depth[i] + 1
            res += nums[i] * weight
        return res
        
        
        
        
        
        