class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = [None] * 26

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if not node.children[ord(c) - ord('a')]:
                    node.children[ord(c) - ord('a')] = TrieNode()
                node = node.children[ord(c) - ord('a')]
            node.word = word

        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.findWord(board, res, i, j, root)

        return res

    def findWord(self, board, res, i, j, node):
        if node.word != "":
            res.append(node.word)
            node.word = ''

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] == '#':
            return False

        c = board[i][j]
        node = node.children[ord(c) - ord('a')]

        if not node:
            return

        board[i][j] = '#'
        self.findWord(board, res, i+1, j, node)
        self.findWord(board, res, i-1, j, node)
        self.findWord(board, res, i, j+1, node)
        self.findWord(board, res, i, j-1, node)
        board[i][j] = c
