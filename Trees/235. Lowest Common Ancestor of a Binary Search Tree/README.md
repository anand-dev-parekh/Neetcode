# 235. Lowest Common Ancestor of a Binary Search Tree

### Medium

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

## Solution

In a BST, for any given node, all the nodes in its left subtree have values less than the node’s value, and all the nodes in its right subtree have values greater than the node’s value. So, if we start at the root of the BST, we can continue to go down the tree until we find the LCA.

There are three possible scenarios:

1. Both p and q are less than the current node: This means both nodes lie in the left subtree of the current node. Move to the left child.
2. Both p and q are greater than the current node: This means both nodes lie in the right subtree of the current node. Move to the right child.
3. ne of p or q is on one side and the other is on the other side, or one of them is the current node: This means the current node is the lowest common ancestor. (return here)
