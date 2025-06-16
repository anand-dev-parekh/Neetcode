# 55. Jump Game

#### Medium

https://leetcode.com/problems/jump-game/

## Solution

A greedy approach to this question is to check at each index whether it was possible to get here from the past indices. And continue to do this until we reach the end of the array. But how do we know if it was possible? Well we can update a variable which contains the max jump distance. If the max jump distance is less than the current index then we know it would fail at this point and we return false. However, if it is greater than or equal, then it is still possible and we must update our max jump distance variable. We update our max jump distance variable to be max(max_jump_distance, cur_index + arr[cur_index]). After iterating the array we then can return whether the max_jump_distance >= length of array.
