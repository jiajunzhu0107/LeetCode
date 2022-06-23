# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            # print(node.val)
            if node.val > p.val and node.val > q.val:
                # print('larger')
                node = node.left
            elif node.val < p.val and node.val < q.val:
                # print('lesser')
                node = node.right
            else:
                # print(node.val)
                return node