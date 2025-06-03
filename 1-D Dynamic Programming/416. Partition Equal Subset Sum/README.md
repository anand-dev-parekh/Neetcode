# 416. Partition Equal Subset Sum

#### Medium

https://leetcode.com/problems/partition-equal-subset-sum/

## Solution

An important piece of information to recognize in this question is that the two subsets sum should equal too eachother.
Therefore, if we were to sum both of these subset sums up, it would equal the total sum of the list.
A easier goal to find for this question is a subset that sums to TOTAL_SUM / 2.

We can see a clear backtracking solution where we recursively add each element to a sum variable or not -> move to next index. This leads to a O(2^N) solution which we can improve upon using DP.
This may seem identical "322. Coin Change", however we do not have a infinite supply of each number (coin) in our list.
Therefore, if we create a DP array of size partition_sum + 1, how do we make sure we do not use a number in nums more than the given amount.

The key to this is to switch the inner and outer loops. We loop through all the numbers in the input nums array, and in our inner loop, loop through our DP array. To avoid any number from being counted twice, we loop in decreasing order and update dp[i] = dp[i] or dp[i-cur_num].

#### Why this works?

This avoids duplicates because dp[i] can only be set to True in two ways,

1. dp[i] is either already set to True, of which it doesn't matter because something already satisfied this sum.

2. do[i-cur_num] is true. i-cur_num < i, so i-cur_num was set by numbers excluding our current number since we increment in decreasing order for our DP array.
