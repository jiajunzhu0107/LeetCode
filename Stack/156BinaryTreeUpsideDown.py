# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if node is None:
            return node
        stack = []
        while node.left:
            stack.append(node)
            node = node.left
        # print(stack)
        if not stack:
            return node
        new_root = stack[-1].left
        while stack:
            node = stack.pop()
            # print(node.val)
            node.left.right = node
            node.left.left = node.right
            node.left = None
            node.right = None
        return new_root