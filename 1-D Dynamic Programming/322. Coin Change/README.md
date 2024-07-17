# 322. Coin Change

### Medium

https://leetcode.com/problems/coin-change/

## Solution

The idea behind this question is to utilize DP tabulation. Given a value worth x amount, assume that all values from 1 to x have a value indicating the minimum number of coins needed to make up that amount. How can we find the minimum number of coins needed for the amount x?

The approach is straightforward: for each amount i from 0 to amount, we loop through all the coins in the coins array. For each coin, we update the DP array to reflect the minimum number of coins needed to make up the amount i by considering the value i - coin. This helps us build up the solution for the amount by using previously computed solutions for smaller amounts. Finally, we can return the last element in our DP array which will be amount x minimum number of coins.