# 198. House Robber

### Medium

https://leetcode.com/problems/house-robber/

## Solution


This question can be solved with DP, similiar to the Easy 1-D Neetcode questions as well. Given and end of a neighborhood, how can you evaluate the the max money it could have gotten? It would either be:

1. If you rob the current house, you cannot rob the previous house, but you can add the current house's money to the maximum money robbed up to the house before the previous one.
2. If you do not rob the current house, the maximum money robbed up to this house is the same as the maximum money robbed up to the previous house.

So the simple solution is to continue to store and update the previous house maxes until you reach the end of the neigborhood. Afterwards, we have the max value we can rob and return it.