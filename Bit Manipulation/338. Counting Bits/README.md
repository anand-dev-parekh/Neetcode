# 338. Counting Bits

#### Easy

https://leetcode.com/problems/counting-bits/

## Solution

For this question, we could simply iterate each number from 0 to n and use our solution to "191. Number of 1 Bits". This is techincally a O(n) solution as each number is 32 bits so we have constant 32 operations per number at max. However, we can optimize this solution using dynamic programming. If we bitshift any integer to the right by one, the result will always be less than or equal the original value. Further, the amount of 1 bits in this result will only differ to the original value by at most 1, which we can account for by using the AND operator with 1 on the original value.

Thus, rather than recomputing and checking the 32 bits again, we can simply use our output list as DP and set our recurrence as such: dp[num>>1] + (num & 1). This eliminates the need for the 32 operations we must do every iteration into just 1.
