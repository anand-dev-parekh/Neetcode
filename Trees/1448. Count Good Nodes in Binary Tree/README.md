# 1448. Count Good Nodes in Binary Tree

### Medium

https://leetcode.com/problems/count-good-nodes-in-binary-tree/

## Solution

We can solve this problem using a Depth-First Search (DFS) traversal of the tree. During the traversal, we keep track of the maximum value encountered on the path from the root to the current node. For each node, we check if its value is greater than or equal to this maximum value. If it is, the node is considered good, and we update the maximum value. Then, we recursively call the function on its children and add their results to the return value. The return value is thus the sum of good nodes from the children plus one if the current node is good. The base case occurs when the node is None, in which case we return 0.