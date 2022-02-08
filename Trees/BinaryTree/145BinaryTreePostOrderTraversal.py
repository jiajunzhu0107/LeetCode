# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self,root,res):
        if root is None:
            return
        self.postOrder(root.left,res)
        self.postOrder(root.right,res)
        res.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postOrder(root,res)
        return res