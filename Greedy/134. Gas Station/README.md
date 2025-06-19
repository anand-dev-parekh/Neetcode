# 134. Gas Station

#### Medium

https://leetcode.com/problems/gas-station/

## Solution

If the total gas is greater than the total cost, there is a solution. How do we know this? Lets assume the total gas >= total cost. If we let i be the smallest partial sum of the array: gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i], then we know to set our return index to i+1. Since the partial sum is the smallest, then gas[i+1]-cost[i+1] >= 0. Because otherwise i+1 index would be the smallest partial sum of the array. Thus, the same reason gives that the rest of the array must have a sum >= 0. Thus, all partial sums starting at i+1 must be non negative and since the entire gas > entire cost, we know this will give us a valid position.


Further, in the question, it states that IF there is a solution then it is guaranteed to be unique. So, if we find the smallest partial sum we know the return index that will lead to valid gas station answer (if total_sum > total_cost). Thus, in my solution I iterated the array in backwards direction to find the largest partial sum and return that index.
