# 124. Binary Tree Maximum Path Sum

### Hard

https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

## Solution

To solve this problem, we employ a recursive approach that traverses the tree and computes the maximum path sum for each node. We define a helper function to assist in this recursive computation.

At each recursive call we will check the maximum path check that goes through our node AND the maximum path that can still continue. To get the maximum path that goes through are node we have to compare four different paths:

1. left path value culmination + current node value
2. left and right path value culmination + current node value
3. right path value culmination + current node value
4. node value

Taking the maximum value from these four options tells us the max path through our given node. We then take the max value that goes through our given node and copmare it to our global answer variable to set the max path sum we have found. However, we still need to return the maximum path sum that can continue on through our parent nodes. This means we cannot consider option 2 from this and must return the max from option 1, 3, and 4.