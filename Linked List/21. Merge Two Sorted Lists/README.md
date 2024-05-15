# 21. Merge Two Sorted Lists

### Easy

https://leetcode.com/problems/merge-two-sorted-lists/description/

## Solution

Because both lists are sorted, the minimums are the beginning nodes. Therefore, we should continue adding the current minimum node (head of l1 or l2) to our output list. And by adding, we should move the pointer of the minimum list to its next node and set the output node to point to our minimum node we found. We should keep doing this until either l1 or l2 is None of which we just add the list that is not None to the output list. This essentially reorganizes our list into a merged sorted list which we return the head of.