# 300. Longest Increasing Subsequence

### Medium

https://leetcode.com/problems/longest-increasing-subsequence/

## Solution

The dynamic programming solution to this question is pretty intuitive. At a given index i, how can we find out the longest increasing subsequence? Well the answer would be the max subsequence from indices 0 to i-1 plus 1 to account for the additional number. This assumes also that the value at i must be greater than the value at the indice from 0 to i-1.

This right here is the subproblem we need to solve this using DP. We set up an dp array equal to length of nums array and store the max subsequence that goes through each indice. We go bottom up so start with indice 0 -> len(nums). And we return the max from dp which is the longest increasing subsequence.