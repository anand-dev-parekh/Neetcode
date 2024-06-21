# 199. Binary Tree Right Side View

### Medium

https://leetcode.com/problems/binary-tree-right-side-view/

## Solution

To solve the problem of finding the right side view of a binary tree, we can use the BFS (Breadth-First Search) OR DFS (Depth-First Search) approach. However, for this question I used BFS which ensures that we visit each level of the tree in order. The right side view of the binary tree is the set of nodes visible when the tree is viewed from the right side. To achieve this, we need to capture the last node's value at each level.

We use a while loop that continues as long as there are nodes in the queue. This ensures that we process every level of the tree. At each level, we determine the number of nodes by checking the length of the queue. This tells us how many nodes are at the current level.

We iterate over all nodes at the current level. For each node: We pop the node from the front of the queue. We update the last element of our result list with the current node’s value. This is because we want the last node in each level, which represents the rightmost node when viewed from the right side. We then add the current node’s children to the queue to be processed in the next level. First the left child, then the right child. This order ensures that the rightmost node at each level is processed last.
