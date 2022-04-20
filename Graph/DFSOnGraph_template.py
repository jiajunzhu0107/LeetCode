# def dfs(root, visited):
#     for neighbor in get_neighbors(root):
#         if neighbor in visited:
#             continue
#         visited.add(neighbor)
#         dfs(neighbor,visited)

def dfs(root, visited):
    visited.add(root)
    print(root)
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        # visited.add(neighbor)
        dfs(neighbor,visited)