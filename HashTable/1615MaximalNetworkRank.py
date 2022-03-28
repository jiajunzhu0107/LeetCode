# https://leetcode.com/problems/maximal-network-rank/
from itertools import combinations
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = {
            i:set() for i in range(n)
        }
        
        for road in roads:
            degree[road[0]].add(road[1])
            degree[road[1]].add(road[0])
        
        max_rank = 0
        # print(degree)
        for a, b in combinations(range(n),2):
            max_rank = max(max_rank, len(degree[a]) + len(degree[b]) - (1 if b in degree[a] else 0))
            
        return max_rank