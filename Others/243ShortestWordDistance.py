class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx_word1 = None
        idx_word2 = None
        dist = inf
        for idx, w in enumerate(wordsDict):
            # print(idx_word1, idx_word2)
            if w == word1:
                idx_word1 = idx
            elif w == word2:
                idx_word2 = idx
            else:
                continue
            if idx_word1 is not None and idx_word2 is not None:
                # print(idx_word1, idx_word2)
                dist = min(dist, abs(idx_word1 - idx_word2))
                if dist == 1:
                    return dist
        return dist