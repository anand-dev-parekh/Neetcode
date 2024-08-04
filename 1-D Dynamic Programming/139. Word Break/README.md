# 139. Word Break

### Medium

https://leetcode.com/problems/word-break/

## Solution

The idea behind this question is to utilize a array (DP) that stores whether at index i, it could have been created using wordDict. Basically at every index that is true in array (index 0 starts as True), we will compare every word in wordDict to the remaining characters in the string. IF they are equal then we can set dp[i] to be true. We continue to do this throughout the array and will return whether the last value in the dp array is true, so whether or not the string can be created with the wordDict or not.