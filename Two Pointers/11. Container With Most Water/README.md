# 11. Container With Most Water

#### Medium

https://leetcode.com/problems/container-with-most-water/description/

## Solution

#### Area Calculation

The area of water contained by two arbitrary points will be limited by the smallest value between the two points. So, the calculation of the area of water is == min(two points) \* (i-j).

#### Two Pointer

We can use a two pointer approach for this question starting at the beggining and end of the array. If you calculate the area at two points you will have two cases.

Case 1: right pointer is >  
If the right pointer is greater, there is no reason to shift it down. As shown in the area calculation, the minimum point defines the height. Therefore, shifting the right pointer down by any value would be meaningless as the height would never get LARGER than the left pointer, and the length would continously shrink. However, shifting the left pointer up one means the height CAN change.

Case 2: left pointer is >=  
WLOG basically the same thing but we shift the right pointer down now.
