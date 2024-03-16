# 36. Valid Sudoku

#### Medium

https://leetcode.com/problems/valid-sudoku/description/

## Solution

This question is just implementation. We will use two for loop from 0:9->0:9, and check all rows, columns, and squares for duplicates using a 3 corresponding sets. Note, to optimize memory slightly you could use arrays of length 9.

#### Row and Columns

These are the most simple. We can just iterate each row/column in the same loop by switching the order of iterator variables i and j to account for iterating rows and columns. For each inner loop we will check if the element already exists in correspoding set. If it does we return False, else we add the element to the set and continue to the next. At the end of each inner loop we should clear out both sets and repeat the process above.

#### Squares

For squares, it is a little bit more complex, but we can use the same two loops for Rows and Columns with the calculation below:

calc_i = ((i // 3)\*3) + (j % 3)

calc*j = ((i%3) * 3) + j//3

We use the same technique used in row and columns and check if it exists in its corresponding set. If it does exist we return false, else we add it to the corresponding set. At the end of each inner loop, which means we checked a full square, we clear the set and move on to the next one.
