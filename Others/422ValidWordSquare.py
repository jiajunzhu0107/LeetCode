# https://leetcode.com/problems/valid-word-square/
# https://techdevguide.withgoogle.com/resources/former-interview-question-word-squares/#!
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # for i in range(len(words)):
        #     len_word = len(words[i])
        #     try:
        #         vert_word = ''.join([words[j][i] for j in range(len_word)] )
        #     except IndexError:
        #         return False
        #     if vert_word != words[i]:
        #         return False
        # return True
        for i in range(len(words)):
            vert_word = []
            for j in range(len(words)):
                if i < len(words[j]):
                    vert_word.append(words[j][i])
            if ''.join(vert_word) != words[i]:
                return False
        return True
