# 141. Linked List Cycle

### Easy

https://leetcode.com/problems/linked-list-cycle/

## Solution

The simple solution to this question is to use a Hashmap/Dictionary and loop through the nodes. If a node has ever been seen before you return True that there is a loop, else you add your node to the Hashmap and continue to the next node. However, can we come up with a solution with O(1) space? Yes, we can with a fast and slow pointer.

Fast Pointer: Every iteration we will move the fast pointer two nodes

Slow Pointer: Every iteration we will move the slow pointer one node


The pointers start at the same place. So if there is NOT a cycle, the fast pointer will reach NULL/the end of list first ALWAYS. However, in the case of a cycle, the fast pointer will eventually catch back up to the slow pointer after it loops. And because it moves two nodes, it will never go past/skip over the slow pointer. So, we can simply check every iteration if the fast pointer == slow pointer. If it is equal we know there is a loop and we can return True.