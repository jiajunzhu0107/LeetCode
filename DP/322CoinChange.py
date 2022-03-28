# https://leetcode.com/problems/coin-change/
# https://algo.monster/problems/coin_change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt_lst = [float(inf)] * (amount + 1)
        amt_lst[0] = 0
        def amt_cal(i):
            if i < 0:
                return float('inf')
            else:
                return amt_lst[i]
        
        for i in range(1,len(amt_lst)):
            amt_lst[i] = 1 + min(
                [amt_cal(i - j) for j in coins]
            )
        print(amt_lst)
        if amt_lst[-1] == float('inf'):
            return -1
        return amt_lst[-1]
            
        
        
        
        