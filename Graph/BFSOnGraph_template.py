# https://algo.monster/problems/graph_bfs

from collections import deque

# def bfs(root):
#     queue = deque([root])
#     visited = set()
#     while len(queue) > 0:
#         node = queue.popleft()
#         for neighbor in get_neighbors(node):
#             if neighbor in visited:
#                 continue
#             queue.append(neighbor)
#             visited.add(neighbor)

def bfs(root):
    queue = deque([root])
    visited = {root}
    
    while len(queue) > 0:
        node = queue.popleft()
        print(root)
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)