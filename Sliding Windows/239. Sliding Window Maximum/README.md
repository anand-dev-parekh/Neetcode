# 239. Sliding Window Maximum

#### Hard

https://leetcode.com/problems/sliding-window-maximum/

## Solution

This question is clearly a sliding window question as we want to find the maximum of each sliding window.
But how can we keep track of this maximum. Of course we could iterate the window every iteration, but this leads to a O(N*k) solution which we can optimize. Is there a data structure we can use to store the maximum for each window?

#### Idea 1: min heap

The min heap idea is simple: we use a min heap to keep track of the elements in each window. As we move to the next window, we add the next element and need to remove the element that is exiting the window.

However, we cannot directly remove arbitrary elements from a min heap efficiently. To work around this, we store each element along with its index in the heap. Then, for each window, we repeatedly pop the minimum element from the heap until its index is within the current window. This ensures that the top of the heap always contains the minimum value for the current window. We then move on to the next window and repeat the process.

#### Idea 2: montonic decreasing deque

A min heap has O(logn) appends and pops. We can do better than this and get our total runtime down to just O(n).
We use a deque to maintain a monotonically decreasing sequence of elements. If we encounter an element in the array that is greater than all previous elements, then it is a fact that those previous elements no longer matter for determining the maximum in the window. Therefore, we can remove them from the deque.

At each step, we remove elements from the back of the deque until either the deque is empty or we find an element greater than the current one. Then, we append the current element along with its index to the deque (to ensure it’s within the window range).

We also remove elements from the front of the deque (which holds the largest values) if they fall outside the current window. Since we always add the current element, it's guaranteed that at least one valid index will be in the deque. The front of the deque then represents the maximum value for the current window.
