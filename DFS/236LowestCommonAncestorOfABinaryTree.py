# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#this is not the standard solution of finding LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = []
        path_q = []
        
        stack = [(root,[root])]
        while stack:
            node,path = stack.pop()
            # print(node.val)
            # if node.val == 5:
                # print(node.val, p.val)
            if node.val == p.val:
                # print(path)
                path_p = path
            elif node.val == q.val:
                path_q = path
            if path_p and path_q:
                break
            for child in [node.left, node.right]:
                if child is not None:
                    stack.append((child,path+[child]))
        common = None
        # print(path_p)
        # print(path_q)
        # return 3
        for i in range(min(len(path_p),len(path_q))):
            if path_p[i].val == path_q[i].val:
                common = path_p[i]
            else:
                break
        return common
                    
        