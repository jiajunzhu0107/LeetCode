# https://algo.monster/problems/visible_tree_node

from math import inf


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(node,max_in_path):
        if node is None:
            return 0
        total = 0
        if node.val >= max_in_path:
            total += 1
        total += dfs(node.left, max(max_in_path, node.val))
        total += dfs(node.right, max(max_in_path, node.val))
        return total
    return dfs(root,-float('inf'))

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
