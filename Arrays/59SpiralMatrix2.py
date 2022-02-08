from copy import deepcopy
from typing import List
# https://leetcode.com/problems/spiral-matrix-ii/
# https://mp.weixin.qq.com/s?__biz=MzI0NjAxMDU5NA==&mid=2475922670&idx=1&sn=c07f56c74d859a7a9d934e3c36488cb9&chksm=ff22f363c8557a75f2e036cb1e0f4bce6fee53ad1ee0012f1ac689703316e88a18c7bd6d49c1&token=1145569493&lang=zh_CN#rd

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        up, down, right, left = 0, n-1, n-1, 0
        val = 1
        while val <= n * n:
            for i in range(left, right+1):
                res[up][i] = val
                print('res in left to right:',res)
                val += 1

            up += 1

            for i in range(up, down+1):
                res[i][right] = val
                val += 1
            right -= 1

            for i in range(right, left-1, -1):
                res[down][i] = val
                val += 1
            down -= 1

            for i in range(down, up-1, -1):
                res[i][left] = val
                val += 1
            left += 1
                # print(res)
        
        return res

if __name__ == '__main__':
    obj = Solution()
    n = 3
    # obj.generateMatrix(n)
    a = [0] * n
    print(a)
    a[0] = 1
    print(a)
    print(a[0] is a[1])

    a = [(0,1,2)] * n
    print(a)
    # a[0][0] = 99
    print(a)
    print(a[0] is a[1])

    a = [[0] * n for i in range(n)]
    print(a)
    a[0][0] = 1
    print(a)

    a = b = 0
    a = 1
    print(b)

    a = []
    b = a
    a.append(1)
    print(b)

    a = tuple((1,))
    print(f'{a!r}')
    a = (1,)
    print(f'{a!r}')
    
    a = (1,2)
    b = a
    a = (1,3)
    print(b)
    
    a = [(1,2,3)] *3
    print(a)
    print(a[0] is a[1])
    del a[0]
    print(a)
    print(a[0] is a[1])

    a = [1]
    b = deepcopy(a)
    print(a is b)
    a.append(2)
    print(b)