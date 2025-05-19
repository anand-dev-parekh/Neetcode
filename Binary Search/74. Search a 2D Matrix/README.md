# 74. Search a 2D Matrix

### Medium

https://leetcode.com/problems/search-a-2d-matrix/

## Solution

This is exactly the same as 704 Binary Search, however, now the array is 2D. This does not change much because we can just set the pointers to treat everything like a it was 1D. And when we want to check the value of the middle index, we can preform a simple calculation to convert it into 2D index formatting.

            row_i = m // row_size
            col_i = m - row_size * row_i
