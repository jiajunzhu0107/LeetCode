# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# check discussions for LCA least common ancestor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPathToValue(node, value, path):
            if node is None:
                return path, False
            path[-1][1] = node.val
            if node.val == value:
                return path, True
            path.append(['L',None])
            path, found = findPathToValue(node.left, value, path)
            if found:
                return path, found
            path.pop()
            path.append(['R',None])
            path, found = findPathToValue(node.right, value, path) 
            if found:
                return path, found
            path.pop()
            return path, found
        
        startPath, found = findPathToValue(root, startValue, [[None,None]]) #[[None,2]]
        # print(startPath)
        destPath, found = findPathToValue(root, destValue, [[None,None]]) #[[None,2],[L,1]]
        # print(destPath)
        #find joint node
        startPathNodes = {} #{2:0}
        for idx,p in enumerate(startPath):
            startPathNodes[p[1]] = idx
        joint = [] #[2,0,0]
        for i in range(len(destPath)-1,-1,-1):
            if destPath[i][1] in startPathNodes:
                joint = [destPath[i][1],startPathNodes[destPath[i][1]],i]
                break
        res = []
        for i in range(len(startPath)-1,joint[1],-1):
            # print(startPath[i])
            res.append('U')
        for i in range(joint[2],len(destPath)-1):
            # print(destPath[i])
            res.append(destPath[i+1][0])
        return ''.join(res)
