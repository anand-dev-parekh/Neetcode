# 543. Diameter of Binary Tree

### Easy

https://leetcode.com/problems/diameter-of-binary-tree/

## Solution

Base Case: If the current node (root) is None, return a tuple (0, 0). This represents a height of 0 and a diameter of 0 since there are no nodes in the subtree.

Recursive Case: For each node, we recursively call the helper function on the left and right children. This gives us:

l_edge_max and l_dis_max: The maximum depth and diameter of the left subtree.
r_edge_max and r_dis_max: The maximum depth and diameter of the right subtree.
Compute Current Values:

The maximum depth of the current subtree is 1 + max(l_edge_max, r_edge_max). We add 1 to account for the current node.
The diameter of the current subtree is the maximum of:
l_dis_max: The diameter of the left subtree.
r_dis_max: The diameter of the right subtree.
l_edge_max + r_edge_max: The path that passes through the current node, connecting the deepest nodes of the left and right subtrees.
Return Values: The helper function returns a tuple containing the computed maximum depth and diameter for the current node's subtree.

Finally, the diameterOfBinaryTree function returns the diameter of the entire tree by calling the helper function on the root node and extracting the second value from the returned tuple. If we compare this to question "110. Balanced Binary Tree", the solution used a class variable. We could still have done this in this question (probably would have made this alot simpler), but I thought it would be nice to have both techniques displaced in this repo.