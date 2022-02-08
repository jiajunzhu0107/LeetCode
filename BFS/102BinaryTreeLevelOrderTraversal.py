# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root]) # at least one element in the queue to kick start bfs
        while len(queue) > 0: # as long as there is element in the queue 
            n = len(queue)
            new_level = []
            for _ in range(n):
                node = queue.popleft() # dequeue
                new_level.append(node.val)
                for child in [node.left,node.right]: # enqueue children
                    if child is not None:
                    # if OK(child): # early return if problem condition met
                    #     return FOUND(child)
                        queue.append(child)
            res.append(new_level)
        return res