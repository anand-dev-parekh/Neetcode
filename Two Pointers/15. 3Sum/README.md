# 15. 3Sum

#### Medium

https://leetcode.com/problems/3sum/description/

## Solution

#### Naive Solution: O(n^3)

The naive solution to this question is to use 3 for loops and check every
possible combination of numbers. This will surely lead to the a correction
answer as we simply loop through every possible combination.

#### Two Pointers: O(n^2)

We can do better than this. First we will sort the array with whatever builtin
function available in your language. This allows us then to check for each number in the array, and only do one additional loop using two pointers because the rest of the array is sorted.
If the current sum of the number and the two pointers is less than 0, then we know to move our left pointer up since its impossible to have a sum with that number. This is the same logic for the right pointer when the sum is greater than 0, we move right pointer down.
