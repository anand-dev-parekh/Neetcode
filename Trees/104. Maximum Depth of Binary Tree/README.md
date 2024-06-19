# 104. Maximum Depth of Binary Tree

### Easy

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

## Solution

This question can be understood with a informal induction proof.

Base Case: Empty Binary Tree will always be length of 0.

Inductive Step: We will assume this to be true with n nodes and show it works for n + 1 nodes. If we add one node to the binary tree at the top, then the maximum height will increase by 1. So we can take the old maximum height from the induction hypothesis and add one to get the new height. Thus, we have the height of n+1 node binary tree.

Thus, in implementation we should add one to the left or right subtree height (which ever is greater).