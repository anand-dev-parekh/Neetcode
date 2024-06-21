# 110. Balanced Binary Tree

### Medium

https://leetcode.com/problems/balanced-binary-tree/description/

## Solution

This question requires us to return a boolean value based on whether the heights of the root subtree ever differ by more than one. If we attempt to solve this question recursively, we would either have to return tuples (one for the height and one for whether the subtree heights ever vary by more than one). Alternatively, my approach is to store a class variable and set it if the tree is ever found to be unbalanced. This approach is simple because it essentially repeats the maximum depth question (104) but adds a check to see if the heights ever differ by more than one.