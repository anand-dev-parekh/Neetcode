class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
            if board[i][j] != word[k]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'
            ans = backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1)
            board[i][j] = tmp
            return ans

        for i, row in enumerate(board):
            for j, c in enumerate(row):

                if backtrack(i, j, 0):
                    return True
        return False
