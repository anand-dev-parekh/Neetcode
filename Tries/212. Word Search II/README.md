# 212. Word Search II

#### Hard

https://leetcode.com/problems/word-search-ii/

## Solution

We were able to solve "79. Word Search" with backtracking. We would iterate each index in the list and recursively try to find a match with the target word (O(m*n*3^L), where L is the length of the word. However, in this problem, we have a list of words which would increase our time complexity to: O(m*n*k*3^L).

However, rather than iterating each word and then running the dfs, we can construct a trie of all of the words. Therefore, for each iteration we check to see if there are any paths in the trie that satisfy the current character. If so, we make our recursive calls same as "79. Word Search". Otherwise, no words in our list even match this pattern so we can terminate the branch. This brings the time complexity down to O(m*n*3^L), where L is the maximum length word in the words list.
