# 572. Subtree of Another Tree

### Easy

https://leetcode.com/problems/subtree-of-another-tree/

## Solution

This question uses the same logic as "100. Same Tree", but now we check every node of root to see if there is a possible subtree. So, the answer is split into two recursive functions. One is to check if two trees are equal (exact same code as "100. Same Tree"). The second function is to recursively go through root and call the IsEqual function to see if there is a subtree equal to subRoot.