# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        fib_lst = [0,1]
        if n < 2:
            return n
        for i in range(2,n+1):
            fib_lst.append(fib_lst[i-2] + fib_lst[i-1])
        return fib_lst[n]