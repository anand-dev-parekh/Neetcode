# 167. Two Sum II Input Array is Sorted

#### Medium

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Solution

Because the array is sorted, we can use a two pointer approach.

Case 1:
So, if the values at the left pointer and right pointer sum to something greater than the target -> We shift the right pointer down by one since no target can be found using the right most value since its too big.

Case 2:
However, if the sum is less than the target -> We shift the left pointer up by one since no target can be found using the left most value since it is too small.

These two cases continously shrink the array/window until it will find the exact solution because there guaranteed is to be one exact solution in the window.
