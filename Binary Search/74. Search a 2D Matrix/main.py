class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        row_size = len(matrix[0]) 

        l = 0
        r = len(matrix) * row_size


        while l < r:
            
            m = (l+r) // 2

            row_i = m // row_size
            col_i = m - row_size * row_i

            if matrix[row_i][col_i] < target:
                l = m+1
            else:
                r = m

        row_i = l // row_size
        col_i = l - row_size * row_i

        if row_i >= len(matrix) or col_i >= row_size:
            return False

        return matrix[row_i][col_i] == target 