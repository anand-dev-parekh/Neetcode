# 100. Same Tree

### Easy

https://leetcode.com/problems/same-tree/

## Solution

This question can be solved with DFS easily, however, the point is that you must make sure you move down the same path of BOTH trees. Whether you implement pre-order, in-order, or post-order it must be recursively call the same subtrees. And the exit condition will be when you reach the bottom of the tree (SUCCESS) OR the nodes are mismatched (FAIL).