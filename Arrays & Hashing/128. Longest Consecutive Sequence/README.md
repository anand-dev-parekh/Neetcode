# 128. Longest Consecutive Sequence

#### Medium

https://leetcode.com/problems/longest-consecutive-sequence/description/

## Solution

The idea behind this question is to use a hashmap and continously update the lengths of the connected sequences. We will do this by storing the lengths of the connected sequence in the boundaries of the window.

So, for n in nums, we should check our map for n-1 and n+1. Thus, the length of the current window at n will be equal to map[n-1] + map[n+1] + 1, because we are combining the left and right window and adding something in the middle.

Thus we can update map[n], but how do we update the rest of the map? For example, if there was a sequence of 2 at n+1, it would now be 3 with the addition of n to the map. Rather than updating all the values in the map, we only really care about the boundaries of the sequence. This is because any other number in the array will NEVER be able to see the values in the middle of the sequence. So after setting map[n] we only have to update the value furthest left in the sequence and the value furthest right in the sequence. In the end, we can return the maximum value in the map as the longest sequence we found.
