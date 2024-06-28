# 297. Serialize and Deserialize Binary Tree

### Hard

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

## Solution

In this question, the way I solved this is to use BFS to serialize the TreeNode into a string. And on the deserialize use a reverse BFS to convert the string we have into a TreeNode.

#### Serialize

To serialize the TreeNode, we will list the nodes in the order we traverse them in BFS. We need to encode this into a string. To represent a new value in the list, we can have a buffer character represented as "d". This is needed because node values can be longer than one digit, so we need some buffer to represent a new node value in our string. Another thing to note is that we must store nodes that are NULL/None, which we do by representing their value with the character "n" instead of the root value.

#### Deserialize

To deserialize, we first split the string based on the buffer character "d". Now, we have a list of values of the tree in BFS order. To convert this back into a TreeNode binary tree, we use a pointer and a queue. The queue will append nodes in the order of BFS. Whenever a node is popped from the queue, its children will be set and appended to the queue using the pointer (as the array is implicitly already in level/BFS order).

