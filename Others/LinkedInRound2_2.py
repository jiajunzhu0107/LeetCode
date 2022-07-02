
 * Given a tree with an arbitrary number of children, sort the nodes by the order in which they would "fall" off a tree.
 * At every step, all the nodes which have no children are deleted from the tree.
 * This process is repeated until only the root node remains, at which point it falls off the tree as well.
 *             A
 *         /   |    \
 *        B    C      D
 *       / \         
 *      E   F      
 *
 * At the first step, leaves "E", "F", "C" and "D" fall off the tree. That leaves us with the following:
 *             A
 *         /  
 *        B 
 * At the second step, only leaf "B" falls off the tree.
 * At the third step, the root "A" falls off the tree.
 *
 * Therefore, for the example tree this method should return: [(E,F,C,D), (B), (A)]
 *
 */

 *             A
 *         /   |    \
 *        B    C      D
 *             / \         
 *              E   F      
            /
            G
```
public List<Set<TreeNode>> fallingLeaves(TreeNode root) {
  // implementation...
}
  
// Reminder of some the useful methods of the TreeNode interface
public interface TreeNode {
  // Get all the children of a node
  Collection<TreeNode> children();
}
```

class TreeNode:
    def __init__(self, value, children: list) -> None:
        self.children = children    # list of TreeNode; empty means leaf node []
        self.val = value
 
    def __str__(self) -> str:
        return f"{self.val}"
 
    def __repr__(self) -> str:
        return f"{self.val}"
 

# None []
# A [[A]]
# A B [[B], [A]]
# A BC [[B,C], [A]]
# A BC E [[B,E],[C],[A]]

# Space complexity O(N)
# Time complexity O(N)
def fallingLeaves(root: TreeNode) -> list:
    output = []
    def dfs(node):
        max_depth = 0
        for child in node.children:
            depth = dfs(child)
            max_depth = max(depth, max_depth)
        node_depth = max_depth + 1
        if len(output) < node_depth:
            output.append([node])
        else:
            output[node_depth-1].append(node)
        return node_depth

    if root is None:
        return output
    dfs(root)
    return output
    

*             A
*         /   |    \
*        B    C     D
*       /  \  |     |
*      E     F -- G 

# direted edge?
{"G":1}

