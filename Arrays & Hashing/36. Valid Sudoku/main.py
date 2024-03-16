class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in range(9):

            row_set = set()
            col_set = set()
            sqaure_set = set()

            for j in range(9):

                if board[i][j] in row_set and board[i][j] != '.':
                    return False

                if board[j][i] in col_set and board[j][i] != '.':
                    return False

                calc_i = ((i // 3)*3) + (j % 3)
                calc_j = ((i%3) * 3) + j//3
                if board[calc_i][calc_j] in sqaure_set and board[calc_i][calc_j] != '.':
                    return False

                col_set.add(board[j][i])
                row_set.add(board[i][j])
                sqaure_set.add(board[calc_i][calc_j])

            row_set.clear()
            col_set.clear()
            sqaure_set.clear()

        return True
