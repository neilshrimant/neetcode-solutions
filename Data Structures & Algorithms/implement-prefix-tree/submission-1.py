class TrieNode:
    def __init__(self):
        self.trie = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.trie:
                curr.trie[w] = TrieNode()
            curr = curr.trie[w]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.trie:
                return False
            curr = curr.trie[w]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.trie:
                return False
            curr = curr.trie[w]
        return True
        
        
        