# 53. Maximum Subarray

#### Medium

https://leetcode.com/problems/maximum-subarray/

## Solution

For this question, you could simply look through every possible subarray and record the max.
But rather, we can use a greedy O(n) runtime approach for this question. While iterating the array, we can keep track of a current sub array sum using a variable: cur_sum. IF the cur_sum + current number is less than the current number itself, then we can simply ignore all sub arrays with the previous numbers and set cur_sum = current_number.

This allows us to see all viable subarrays but how do we know which one is the maximum. What if the maximum is in the beginning of the array and then there are many negative numbers?

Example: [100, -12, -23, -2]

The cur_sum variable will be by iteration: 100, 88, 65, and then 63. To compensate for this, we will hold a max_subarray variable that simply stores the maximum subarray that we find.
