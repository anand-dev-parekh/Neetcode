# 78. Subsets

#### Medium

https://leetcode.com/problems/subsets/

## Solution

In order to get the power set of an array of unique elements, we generate all subsets. Thus, backtracking would be a good approach to this question. In the problem description it states that the list is made up of unique/distinct elements.

Therfore, given an arbitrary subset, to make it from the list we would iterate each element in the array and make a binary decision:

1. Add it to the subset? (YES OR NO)

We can implement this in our recursive calls. The base case would be when our iterator reaches the end of the array (We add the current subset to output array). And we would make two recursive calls where in one we add the current element to the current subset and the other we skip the current element. Thus, after calling this function starting at index 0, we can return our output array.
