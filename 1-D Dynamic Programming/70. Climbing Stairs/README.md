# 70. Climbing Stairs

### Easy

https://leetcode.com/problems/climbing-stairs/

## Solution

This question is very similiar to fibonacci. If we are at some stair case x, how do we know how many unique ways there are to get to it? Because we can only move up 1 or 2 staircases, the answer would be all the unique combinations of stair x-1 + stair x-2. So, the simple O(n) solution to this is to store two variables keeping track of the previous two stairs unique combinations as we move up. Finally, when we reach stair n we can compute unique ways by adding the previous two stair cases and return the sum.