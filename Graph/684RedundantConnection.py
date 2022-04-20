# https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        def dfs(v1, v2):
            if v1 in visited:
                return False
            if v1 == v2:
                return True
            visited.add(v1)
            for v in graph[v1]:
                if dfs(v, v2):
                    return True
            return False
        for v1, v2 in edges:
            visited = set()
            if v1 in graph and dfs(v1, v2):
                return [v1, v2]
            if v1 in graph:
                graph[v1].add(v2)
            else:
                graph[v1] = {v2}
            if v2 in graph:
                graph[v2].add(v1)
            else:
                graph[v2] = {v1}