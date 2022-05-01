# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node):
            if node is None:
                return 
            if low <= node.val <= high:
                self.res += node.val
            if node.val < high:
                traverse(node.right)
            if node.val > low:
                traverse(node.left)
            return
        self.res = 0
        traverse(root)
        return self.res

#######################stack####################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root):
            if root is None:
                return 
            stack = [root]
            while stack:
                node = stack.pop()
                if low <= node.val <= high:
                    self.res += node.val
                if node.val > low and node.left:
                    stack.append(node.left)
                if node.val < high and node.right:
                    stack.append(node.right)
                
            return
        self.res = 0
        traverse(root)
        return self.res