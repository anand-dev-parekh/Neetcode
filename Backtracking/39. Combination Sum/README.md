# 39. Combination Sum

### Medium

https://leetcode.com/problems/combination-sum/

## Solution

This question seems very simple at first. At each node in our recursive tree we could add each element in the candidates array as a child node and continue to do so until subset_sum == target or subset_sum > target. However, the problem with this is that we will get duplicates (different permutations) and we only want to return unique combinations.

#### Unique combinations

In order to get unique combinations, we can use the fact that the list is made up of UNIQUE elements itself. Therefore, if we make only branch on the numbers that are further along in the array, then we will never have duplicates (since the array has no duplicates). Therefore, in each recursive call, we iterate the numbers with indices greater than or equal to the current index and make our recursive calls. Our base case is simply the same as above, when subset_sum == target or subset_sum > target.
