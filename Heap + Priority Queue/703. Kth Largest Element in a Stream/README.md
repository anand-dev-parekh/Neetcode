# 703. Kth Largest Element in a Stream

### Easy

https://leetcode.com/problems/kth-largest-element-in-a-stream/

## Solution

The idea to achieve O(logn) add time is to use a priority queue. In Python, we can utilize the heapq module to heapify the initial array.

#### __init__

This allows us to continously pop the minimum values from the heap, until there is just k elements in the heap. This means our heap's minimum value (at index 0 in the array) will be the kth largest element. This assumes that the initial array had a size >= k. What if the initial array's size was much smaller? Then by the bounds of the question, the size of the heap will be one less than the k. And when we add a new element, there will be enough values in the array for there to exist an "kth largest element".

#### add

In this part, we will utilize the heap we have stored from the init function and heappush the new element into our heap. If the size of our heap is now greater than k, we will heappop one element (the current minimum) so the size is k. Meaning the first element in the array (minimum value in our heap) will be kth largest element and we can simply return that.