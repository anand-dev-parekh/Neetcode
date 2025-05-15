# 42. Trapping Rain Water

#### Hard

https://leetcode.com/problems/trapping-rain-water/

## Solution

If given a arbitrary index on the elevation map, the amount of water that can be placed in that index depends on two factors. It depends on the max height from the left of the index and the max height from the right of the index. It will then take the minimum of these two heights and subtract it to the current index elevation to get the final amount of water that can fitin the arbitrary index.

#### Two Pointers

So, a O(n) solution then is to use two pointers and continously update these max height variables. However, how do we actually know when to move the left and right pointers?

We do this based upon the minimum of the left max height and right max height. Whichever one is smaller is the one that limits the arbitrary indices in the middle. Thus, we move the pointer with the smaller max height and continously update the trapped water.
