# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def contains(self, char):
        return char in self.children
    
    def insert(self, char, node):
        self.children[char] = node
    
    def next(self, char):
        return self.children[char]
    
    def setIsWord(self):
        self.isWord = True
        
    def getIsWord(self):
        return self.isWord
        
class Trie:

    def __init__(self):
        self.data = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.data
        for c in word:
            if not node.contains(c):
                node.insert(c, TrieNode())
                # node[c] = {'#':False}
            node = node.next(c)
        # node['#'] = True
        node.setIsWord()
        

    def search(self, word: str) -> bool:
        node = self.data
        for c in word:
            # if c not in node:
            if not node.contains(c):
                return False
            node = node.next(c)
        return node.getIsWord()

    def startsWith(self, prefix: str) -> bool:
        node = self.data
        for c in prefix:
            # if c not in node:
            if not node.contains(c):
                return False
            node = node.next(c)
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)