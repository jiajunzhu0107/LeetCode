# https://leetcode.com/problems/gas-station/
# https://algo.monster/problems/gas_station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain_gas = 0 #1
        traveled = 0 #5
        res = -1 # 3
        i = 0 #3
        while traveled < len(gas) : 
            if gas[i % len(gas)]+remain_gas < cost[i % len(gas)]:
                i += 1
                if i >= len(gas):
                    return -1
                remain_gas = 0
                traveled = 0
                res = -1
                continue
            if traveled == 0:
                res = i % len(gas)
            remain_gas = remain_gas + gas[i % len(gas)] - cost[i % len(gas)]
            traveled += 1
            # i = (i+1) % len(gas)
            i += 1
        return res
