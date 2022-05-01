# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def delete(self, root, parrent, isLeftChild):
        if root.right:
            stack = [root.right]
            parrent = root
            while stack:
                node = stack.pop()
                if node.left:
                    parrent = node
                    stack.append(node.left)
            root.val = node.val
            if parrent == root:
                self.delete(node, parrent, isLeftChild = False)
            else:
                self.delete(node, parrent, isLeftChild = True)
        elif root.left:
            stack = [root.left]
            parrent = root
            while stack:
                node = stack.pop()
                if node.right:
                    parrent = node
                    stack.append(node.right)
            root.val = node.val
            if parrent == root:
                self.delete(node, parrent, isLeftChild = True)
            else:
                self.delete(node, parrent, isLeftChild = False)
        else:
            if parrent and isLeftChild:
                parrent.left = None
            elif parrent and not isLeftChild:
                parrent.right = None
            root = None
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        stack = [root]
        parrent = None
        isLeftChild = None
        while stack:
            node = stack.pop()
            if key > node.val and node.right:
                stack.append(node.right)
                parrent = node
                isLeftChild = False
            elif key < node.val and node.left:
                stack.append(node.left)
                parrent = node
                isLeftChild = True
            elif key == node.val:
                #delete it
                if node == root and root.left is None and root.right is None:
                    root = None
                else:
                    self.delete(node, parrent, isLeftChild)
        return root
                