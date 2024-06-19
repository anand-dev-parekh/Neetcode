# 19. Remove Nth Node From End of List

### Medium

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Solution


### Two Passes

This question can be solved easily by utilizing two passes. In the first pass, we should record the length of the entire list. With this, we can find how many nodes from the start the node that should be removed is. Then, on the second pass we simply iterate 1 to one node before the node that should be removed and set its next pointer to next.next which effectively eliminates the node that should be removed from the list.

### Can we do this in one pass?

Yes. The way to solve it in one pass utilizes two pointers. These two pointers should iterate the list at the same speed, but start at different points. We will let the "slow" pointer start at the beggining of the list and the "fast" pointer start n nodes ahead of the slow pointer. This way when the fast pointer reaches the end of the list, the slow pointer will be exactly n nodes before the end of the list. And we can repeat the process from above where we set the pointer's next = next.next.