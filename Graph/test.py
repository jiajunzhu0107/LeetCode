graph = {}
a = [[1,2],[3,4]]
for v1, v2 in a:
    graph[v1].add(v2)
    graph[v2].add(v1)
print(graph)