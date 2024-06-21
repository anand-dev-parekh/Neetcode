# 98. Validate Binary Search Tree

### Medium

https://leetcode.com/problems/validate-binary-search-tree/description/

## Solution

We can solve this problem using a recursive function that validates each node while keeping track of allowable value ranges. Each node must fall within a specific range of values to be considered valid. The approach involves recursively checking each node and updating the range constraints accordingly. Our base case is when the node reaches the end of the tree and it is NULL. Otherwise, we must make sure the current node is within the range and that its children nodes both satisfy this (recursively call the children). However, the way we update the range is different for the left and right node. If it is the left node we are calling, then the max_val should be updated to be the current node value as the left node value should never exceed the current node value. This is the opposite for the right side as the min_val should be set to the current node value.