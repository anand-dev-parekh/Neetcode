# 213. House Robber II

### Medium

https://leetcode.com/problems/house-robber-ii/

## Solution

This question is the exact same as "198. House Robber" except now we cannot connect the end and start house as the neighborhood is in a circle. So, the simple solution is to employ 198's solution twice. The first time, we will ignore the first house, and the second time we will ignore the last house. We can simply return the maximum of this operation as houses will always be positive, so the max solution contains the first house or last house for sure (or ignoring first and last house will result in same answer).