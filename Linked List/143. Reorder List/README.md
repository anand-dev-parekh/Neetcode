# 143. Reorder List

### Medium

https://leetcode.com/problems/reorder-list/description/

## Solution

The way you solve this question is a culmination of the Easy tagged questions in this Linked List topic. It should appear that the order is just using two pointers on the edge of the list and moving inwards. However, these are ListNodes without random access so how can you decrement the pointer on the right side of the list? You may think you must create an array of Node pointers to have access to this, but you actually can avoid this O(n) space allocation. We avoid it by reversing the nodes on the right side of the list and then using two pointers to get the zig-zag pattern. Thus, this comes down to three steps:


1. Find midpoint of list (which is done through fast/slow pointer)
2. Reverse the right side of the list
3. Use two pointers to update where each Node points too