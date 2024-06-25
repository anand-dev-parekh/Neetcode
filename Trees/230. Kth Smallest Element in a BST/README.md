# 230. Kth Smallest Element in a BST

### Medium

https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

## Solution

This question can be solved in a manner very similar to "98. Validate Binary Search Tree." We will solve it iteratively in-order as this allows us to see the nodes in non-decreasing order.

We use a while loop to process the nodes. This loop continues as long as there are nodes to visit or nodes in the stack. For each node, we first move to its leftmost child, pushing each node onto the stack (the inner loop). This process ensures that we are following the in-order traversal order. Once we reach a None node, we pop the top node from the stack, which is the next node in the in-order sequence.

Then we subtract 1 from k. If k is equal to 0, we know that this is the kth smallest element, as the previous nodes we have checked out have been the k smallest elements.