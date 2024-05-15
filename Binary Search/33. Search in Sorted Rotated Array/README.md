# 33. Search in Sorted Rotated Array

### Medium

https://leetcode.com/problems/search-in-rotated-sorted-array/

## Solution

This question is similiar to Find Minimum in Sorted Rotated Array (153) except now we are trying to find a target rather than the minimum. Thus, to solve this question in O(logN) time we must use binary search and once again coming up with the cases to split the array will provide the challenge.

When to cut left half of array off?

1. If the target is less than the middle value and less than the right value (then it must be in the right side)
If the middle value is > right value then we know the pivot is in between them, thus
2. If middle value is > right value and target is < right value (it must be before the right value since we know the pivot happens on the right side)
3. If middle value is > right value and target is > mid value (it must be after the middle value since we know the pivot happens on the right side)