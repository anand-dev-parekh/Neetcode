class TrieNode:
    def __init__(self):
        self.word = False
        self.tries = {}

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        node = self.node
        for c in word:
            if c not in node.tries:
                node.tries[c] = TrieNode()

            node = node.tries[c]

        node.word = True
        return

    def search(self, word: str) -> bool:
        node = self.node
        for c in word:
            if c not in node.tries:
                return False

            node = node.tries[c]

        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for c in prefix:
            if c not in node.tries:
                return False

            node = node.tries[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
