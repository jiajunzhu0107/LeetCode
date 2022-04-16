# https://leetcode.com/problems/replace-words/
class Solution:
    class TrieNode:
        def __init__(self):
            self.isWord = False
            self.children = {}
            
    def createTrie(self, dictionary):
        head = self.TrieNode()
        for word in dictionary:
            curr_head = head
            for c in word:
                if c not in curr_head.children:
                    curr_head.children[c] = self.TrieNode()
                curr_head = curr_head.children[c]
            curr_head.isWord = True
        return head
    def findWord(self, word, head):
        res = ''
        for c in word:
            if c in head.children:
                head = head.children[c]
            else:
                return word
            res += c
            if head.isWord:
                  return res
        return res 
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        head = self.createTrie(dictionary)
        res = []
        for word in sentence.split(' '):
            res.append(self.findWord(word, head))
        return ' '.join(res)
    
    

        