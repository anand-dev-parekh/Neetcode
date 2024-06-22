# 98. Validate Binary Search Tree

### Medium

https://leetcode.com/problems/validate-binary-search-tree/description/

## Solution


#### Recursive 

We can solve this problem using a recursive function that validates each node while keeping track of allowable value ranges. Each node must fall within a specific range of values to be considered valid. The approach involves recursively checking each node and updating the range constraints accordingly. Our base case is when the node reaches the end of the tree and it is NULL. Otherwise, we must make sure the current node is within the range and that its children nodes both satisfy this (recursively call the children). However, the way we update the range is different for the left and right node. If it is the left node we are calling, then the max_val should be updated to be the current node value as the left node value should never exceed the current node value. This is the opposite for the right side as the min_val should be set to the current node value.

#### Iterative In Order

By the definition of a Binary Search Tree, if it is traversed In Order, then the values will be seen in non-decreasing order. So, we can traverse the tree In Order and return whether the nodes are non-decreasing or not.

The idea is to perform an in-order traversal iteratively using a stack, which helps manage the nodes we need to visit. We  use a while loop to process the nodes. This loop continues as long as there are nodes to visit or nodes in the stack. For each node, we first move to its leftmost child, pushing each node onto the stack (the inner loop). This process ensures that we are following the in-order traversal order.

Once we reach a None node, we pop the top node from the stack, which is the next node in the in-order sequence. We then check if this node's value is greater than the previous node value. If not, the tree violates the BST property, and we return False. If the current node's value is valid, we update the previous node value and move to the right subtree of the current node.

By continuing this process, we ensure that all nodes are visited in the correct order. If we complete the traversal without finding any violations, we return True, indicating that the tree is a valid BST.