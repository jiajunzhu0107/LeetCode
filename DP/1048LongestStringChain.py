# https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words,key=lambda x:len(x))
        #words = sorted(words,key=len)
        words_index = {w:i for i, w in enumerate(words)}
        dp = [1] * len(words)
        res = 1
        for idx, word in enumerate(words):
            for i in range(len(word)):
                pre = word[:i]+word[i+1:]
                if pre in words_index:
                    dp[idx] = max(dp[idx],dp[words_index[pre]]+1)
                    res = max(res, dp[idx])
        # print(dp)
        return res