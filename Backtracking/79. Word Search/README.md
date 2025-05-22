# 79. Word Search

### Medium

https://leetcode.com/problems/word-search/description/

## Solution

Given a 2D matrix, the word could possibly begin and exist at any of the indices. Thus, a simple backtracking solution would be to recursively check if the word matches starting at every index in the matrix.

#### Recursive Idea

On each recursive call, we must confirm that the word index matches the character in the matrix we are currently at. If it does not, then we can eliminate this path. However, if they do match we must make recursive calls in all four directions horizontally and vertically to check whether the path possibly matches our word. If we reach a point that is >= len(word) then that means there is a match and we can return True.

#### Implementation Details

This idea seems pretty simple however there are some implementation details we must take into account.

1. Checking the indices are within bounds of the 2D matrix of each recursive call
2. Each letter can only be used ONCE. Therefore, before making recursive calls, we temporalily set the value at the current index to '#'. If another recursive call down the same path reaches this index it will not count this again. After the recursive calls are done we restore this value to the original.
3. Make sure to increment the word index k on each recursive call.
