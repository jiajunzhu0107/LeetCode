# https://leetcode.com/problems/word-squares/
# https://techdevguide.withgoogle.com/resources/former-interview-question-word-squares/#!
#backtracking + trie

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        trie = {}
        for index,word in enumerate(words):
            node = trie
            for c in word:
                if c in node:
                    node = node[c]
                else:
                    node[c] = {'#':[]}
                    node = node[c]
                node['#'].append(index)
        def getWordsWithPrefix(prefix):
            node = trie
            for c in prefix:
                if c not in node:
                    return []
                node = node[c]
            return [words[i] for i in node['#']]
        
        def fillBoard(words_current, words):
            if len(words_current) == len(words_current[0]):
                res.append(words_current)
                return
            vert_word = []
            exact = False
            for word in words_current: #word = ball,a
                if len(word) <= len(words_current):
                    exact = True
                    break
                vert_word.append(word[len(words_current)])	#a
            if exact:
                if ''.join(vert_word) not in words:
                    return False
                else:
                    if len(words_current) + 1 == len(words_current[0]):
                        res.append(words_current+[''.join(vert_word)])
                        # print(res)
                        return True
                    else:
                        fillBoard(words_current+[''.join(vert_word)], words)
            else:
                # for w in [word for word in words if word.startswith(''.join(vert_word)) and len(word)<=len(words_current[-1]) ]:
                for w in getWordsWithPrefix(''.join(vert_word)):
                    fillBoard(words_current+[w], words)
            return True

        for word in words: #ball
            fillBoard([word],words)
        return res