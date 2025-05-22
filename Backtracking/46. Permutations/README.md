# 46. Permutations

#### Medium

https://leetcode.com/problems/permutations/description/

## Solution

This question is also very similiar to "39. Combination Sum", "40. Combination Sum II", "90. Subsets II". Except obviously, this time we are looking for all permutations. We need all possible orderings, so in each recursive call, we cannot simply iterate the indices that appear after our current index and make recursive calls.

An important note is that the max length of nums is 6. So, it is a constant time operation to check whether a specific num exists in the subset. Thus, to find all possible orderings, we scan the whole array of nums and only make a recursive call if the num is NOT in our current subset. Then, when our subset is equal in size to the nums array, we append it to our result array (our base case). This succesfully creates a list of all permutations because it branches all possible orderings, but avoids counting any number twice with our constant time "num in subset" check.
