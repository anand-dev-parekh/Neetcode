# 739. Daily Temperatures

#### Medium

https://leetcode.com/problems/daily-temperatures/description/

## Solution

The intuitive O(n^2) solution to this is to iterate the array, and then do a inner loop of all the elements after and check if there is a temperature after > original temperature. However, we can get this down to O(n) by utilizing the stack data structure. The idea is to have the stack keep track of the temperature indices that have NOT found a higher temperature and sorted order by temperature. In each iteration, we will loop through all temperatures in the stack that are less than the current temperature (which is simply popping from the stack until you find a temp >= current temp). Then, we can simply add the current temperature to the stack as it is the new minimum. After each pop in the inner loop, it is garuanteed that the current index is the minimum amount of time to find a higher temperature because every temperature still in the stack has yet to find a higher temperature, thus we can update the output array.