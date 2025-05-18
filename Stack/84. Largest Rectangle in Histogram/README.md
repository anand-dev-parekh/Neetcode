# 84. Largest Rectangle in Histogram

#### Hard

https://leetcode.com/problems/largest-rectangle-in-histogram/

## Solution

For a bar with height h, how can we calculate the max area of it. We can try extending the bar to the left and right until we encounter a bar that has height less than h. But, if we did this operation on EVERY bar, our time complexity would be O(n^2) which is too slow. Rather than computing the left and right boundaries every time, we can actually use a monotonically increasing stack so it is precomputed.

We will let our stack contain the bar heights in increasing order. Thus, if we encounter a bar height that is less than an of the previously bars, then we should continously pop. Why? We do this because those previous bars will always be limited by the current bar's height, so it is useless information to continue to store. However, after we pop, we must calculate the maximum possible area that was possible using that height. We can do this using a simple calculation of the (current_index - j_index) * height.  We know this because j_index through current_index will all have increasing bar heights due to the nature of a monotonically increasing stack. Thus, we simply store a variable and update the maximum area every time it is greater.
