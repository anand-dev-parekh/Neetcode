# 981. Time Based Key-Value Store

### Medium

https://leetcode.com/problems/time-based-key-value-store/

## Solution

The intuition behind this question is to use a Dictionary/Hashmap to store the keys and their corresponding values. Our data structure to store this data can be a <str:[(int, str)]>. So the keys will be a string and the values will be an array of tuples. This allows for O(1) setter method because you simply just add to the array. However, what will the getter method be? One fact we must remember is that the array is strictly increasing based on the timestamp. This should make us think right away to use binary search as our arrays will be sorted. There is one small edge case/trick to consider before implementing however, in this question the target timestamp is not guaranteed to be in the array. Therefore, we must take into account the returning value should be <= target by potentially decrenting the index we end on.