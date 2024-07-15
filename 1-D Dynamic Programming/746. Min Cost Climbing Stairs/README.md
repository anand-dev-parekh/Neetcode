# 746. Min Cost Climbing Stairs

### Easy

https://leetcode.com/problems/min-cost-climbing-stairs/description/

## Solution

This question is also very similiar to "70. Climbing Stairs" and fibonacci sequence. At a given stair x, the minimum cost to reach this stair, would be minimum(stair x-1, stair x-2) + stair x cost. This is once again because we can only move up 1 or 2 stairs at a time. So, to solve this in O(n) time with O(1) memory, we can loop through and update the costs in the actual costs array. And eventually we will go update all stair path costs, and we can return the minimum of the last two stair cases.