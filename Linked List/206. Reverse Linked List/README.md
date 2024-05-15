# 206. Reverse Linked List

### Easy

https://leetcode.com/problems/reverse-linked-list/description/

## Solution

The idea to solve this question is quite intuitive. Either recursively or iteratively move through the list and set each node to point to the previous node. However, actually implementing this can be a little tricky since when you set each node to point to the previous node, you lose reference to the next node in the list. The solution to this issue is to use 2 local variables to store the previous node and next_node so we do not lose references while updating the list.