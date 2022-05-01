# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def findBound(root, target):
            node = root
            low = -inf
            up = inf
            while node:
                if node.val == target:
                    return node.val, node.val
                elif node.val > target:
                    up = node.val
                    node = node.left
                else:
                    low = node.val
                    node = node.right
            return low, up
        low, up = findBound(root, target)
        if abs(low - target) <= abs(up - target):
            return low
        else:
            return up