class TrieNode:
    def __init__(self):
        self.word = False
        self.tries = {}

class WordDictionary:
    def __init__(self):
        self.trienode = TrieNode()


    def addWord(self, word: str) -> None:
        node = self.trienode
        for c in word:
            if c not in node.tries:
                node.tries[c] = TrieNode()
            node = node.tries[c]

        node.word = True
        return

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.trienode)

    def searchHelper(self, word:str, node: TrieNode) -> bool:

        for i, c in enumerate(word):
            if c == '.':
                for j in node.tries:
                    if self.searchHelper(word[i+1:], node.tries[j]):
                        return True
                return False
            if c not in node.tries:
                return False

            node = node.tries[c]

        return node.word




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
