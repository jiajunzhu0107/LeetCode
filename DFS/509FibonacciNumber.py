class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def dfs(n,memo):
            
            if n == 0 or n == 1:
                return n
            if n in memo:
                return memo[n]
            res = dfs(n-2, memo) + dfs(n-1, memo)
            memo[n] = res
            return res
        return dfs(n, memo)            