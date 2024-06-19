# 226. Invert Binary Tree

### Easy

https://leetcode.com/problems/invert-binary-tree/description/

## Solution

There are two ways to solve this question: BFS and DFS.

#### Depth First Search (DFS)

The idea behind this solution is simple. Swap the left pointer with the right pointer, and recursively do this until you reach the bottom. Then you have inverted the tree from the top root all the way to the bottom.

This can be better understood with an informal inductive proof. Assume that whatever node you're at in the recursive process has its left sub tree and right sub tree inverted. Then it is a matter swapping of the left and right pointers to invert the entire tree. And the base case is when the node is == None. Thus, you can assume this will work for height + 1 and so on.

#### Breath First Search (BFS)

In this solution, we will traverse the tree in "level order". This is done iteratively using a queue data structure. This can be broken into _ simple steps

1. Add root to queue
2. While queue is not empty: 
    a. pop MRU node
    b. swap children node pointers
    c. append children nodes to queue
3. return root

*An important thing to note is if the node added is None, you must skip it in the while loop.

Overall, its clear that one is simply inverting the tree but just in a different order.