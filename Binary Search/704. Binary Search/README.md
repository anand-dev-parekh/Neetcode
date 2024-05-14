# 704. Binary Search

### Easy

https://leetcode.com/problems/binary-search/

## Solution

This is a basic binary search question. Rather than iterating the whole array from left to right for the target (O(N)), we can use something called binary search to split the array in halves finding the target (O(logN)). The idea is to set up two pointers on the edges of the array so index 0 and len(nums)-1. We can then calculate the index in the middle of the two pointers and compare it to the target. If the value at the middle index is greater than the target, then we know the target CANNOT be to the right of the middle index (because arr is sorted), thus we can set the right pointer to the middle index. WLOG for when the middle value is less than the target we set left pointer to middle. We can keep doing this until the left pointer is equal to the right pointer and return left index == right index.