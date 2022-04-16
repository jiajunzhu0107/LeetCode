# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, lower_bound = -inf, upper_bound = inf):
            if node is None:
                return True
            
            if not lower_bound < node.val < upper_bound:
                return False
            
            return validBST(node.left, lower_bound, node.val) and validBST(node.right, node.val, upper_bound)
        return validBST(root)
        