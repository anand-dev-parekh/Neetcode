# 153. Find Minimum in Sorted Rotated Array

### Medium

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


## Solution

The obvious solution is to loop through the array and return the minimum value you find. However, we must solve this question in O(logN) time. Thus, binary search should come to mind since the array is sorted kind of? Because the array is sorted AND rotated, the cases we cut the array in half will be different.

Let m represent the index in between left and right pointer and r represent the right pointer index. Since the array is made up of unqiue values our cases can simply be

Case 1: nums[m] > nums[r]

All the values to the left of m will be greater than nums[r], so we can cut this half off and set l = m+1

Case 2: nums[m] <= nums[r]

All the values to the right of m are greater than nums[m] so they cannot be the minimum. Thus, we can cut this half off and set r = m

Thus we have our cases and can return the minimum value.