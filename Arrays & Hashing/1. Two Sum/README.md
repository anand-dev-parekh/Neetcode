# 1. Two Sum

#### Easy

https://leetcode.com/problems/two-sum/description/

## Solution

For this question we utilize a hashmap that stores the values we have seen in the array to their specific index. As we iterate the array, we can check the hashmap to see if the target-current_element is in the hashmap. If it does, that means we have previously seen a value that when added with the current element sums to the target, and thus we can return the current index, and index stored in the hashmap. However, if the target-current_element does not exist in the hashmap, we can add our current element and move to the next element.
