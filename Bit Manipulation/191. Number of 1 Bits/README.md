# 191. Number of 1 Bits

#### Easy

https://leetcode.com/problems/number-of-1-bits/

## Solution

One way to check if our number has a 1 bit in the rightmost position is to use the AND operator with 1.
So, num & 1 will return 1 if there IS a 1 bit in the rightmost position and 0 if there is NOT. However, we want to find out the total number of 1 bits in ALL positions. A simple solution to this then is to cotinously shift our number while it is greater than 0. On each shift, we preform a AND operation with 1 incrementing our counter variable when there is a 1 bit.
