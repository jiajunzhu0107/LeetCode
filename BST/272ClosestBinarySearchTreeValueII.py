# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
# https://algo.monster/problems/closest_bst_values_ii
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inOrderTraversal(root):
            if root is None:
                return
            found = inOrderTraversal(root.left)
            if found:
                return found

            if len(res) == k:
                dist_first = abs(res[0] - target)
                #dist_last = abs(res[-1] - target))
                #max_dist = max(dist_first, dist_last)
                if dist_first <= abs(root.val - target):
                    return True
                res.popleft()
            res.append(root.val)

            return inOrderTraversal(root.right)
        res = deque([])
        found = inOrderTraversal(root)
        return res
