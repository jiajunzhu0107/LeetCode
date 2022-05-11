# https://leetcode.com/problems/shortest-word-distance-ii/
from bisect import bisect_left
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = {}
        for idx, word in enumerate(wordsDict):
            if word not in self.wordsDict:
                self.wordsDict[word] = [idx]
            else:
                self.wordsDict[word].append(idx)
            

    def shortest(self, word1: str, word2: str) -> int:
        shortest_dist = inf
        p1 = 0
        p2 = 0
        while p1 < len(self.wordsDict[word1]) and p2 < len(self.wordsDict[word2]):
            if self.wordsDict[word1][p1] == self.wordsDict[word2][p2]:
                return 0
            elif self.wordsDict[word1][p1] < self.wordsDict[word2][p2]:
                shortest_dist = min(shortest_dist, self.wordsDict[word2][p2] - self.wordsDict[word1][p1])
                p1 += 1
            else:
                shortest_dist = min(shortest_dist, self.wordsDict[word1][p1] - self.wordsDict[word2][p2])
                p2 += 1
        return shortest_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)