# 347. Top K Frequent Elements

#### Medium

https://leetcode.com/problems/top-k-frequent-elements/description/

## Solution

To solve this question, it can be broken down into four steps.

1. Create a frequency map of the elements in nums

2. Turn the map into array<tuples<int, int>>

3. Sort the array of tuples by the frequency or second element in the tuple

4. Return k elements on the right side of the array
