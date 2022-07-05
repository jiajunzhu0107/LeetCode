# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/
# 2135. Count Words Obtained After Adding a Letter
# {3:{a:{c:{t}, {n:t}}}, 4:{a:{c:{k:{t}}}}}

#also can be done by bit mask, check discussion

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_words_sorted = {''.join(sorted(word)) for word in startWords}
        output = 0
        for targetWord in targetWords:
            target_word_sorted = ''.join(sorted(targetWord))
            for i in range(len(target_word_sorted)):
                if (target_word_sorted[:i] + target_word_sorted[i+1:]) in start_words_sorted:
                    output += 1
                    break
        return output
        