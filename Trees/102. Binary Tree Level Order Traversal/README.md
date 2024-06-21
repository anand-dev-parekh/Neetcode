# 102. Binary Tree Level Order Traversal

### Medium

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## Solution

To solve this problem, we need to use BFS (Breadth-First Search) because it iterates through the nodes in "level order." We first initialize a queue to store our nodes. But how do we know which level each node is in?

The solution is to use an inner loop inside the outer while loop that runs as long as the queue is not empty. This approach allows us to pop the nodes incrementally, level by level, rather than continuously. At the beginning of each iteration of the while loop, we get the number of nodes currently in the queue, which represents the nodes at the current level. This number is stored in the variable l.

Thus, we know the inner loop should pop l nodes and append their values to the result array.