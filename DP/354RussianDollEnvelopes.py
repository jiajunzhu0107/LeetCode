# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        def LIS(arr):
            sub = []
            for v in arr:
                i = bisect_left(sub,v)
                if i == len(sub):
                    sub.append(v)
                else:
                    sub[i] = v
            return len(sub)
        return LIS([e[1] for e in envelopes])
        

#this will time out
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         envelopes.sort()
#         # print(envelopes)
#         dp = [1] * len(envelopes)
#         res = 1
#         for i in range(1,len(envelopes)):
#             for j in range(1, i+1):
#                 if (envelopes[i][0] > envelopes[i-j][0]) and\
#                 (envelopes[i][1] > envelopes[i-j][1]):
#                     dp[i] = max(dp[i-j] + 1,dp[i])
#             res = max(res,dp[i])
#         # print(dp)
#         return res

