# 973. K Closest Points to Origin

### Medium

https://leetcode.com/problems/k-closest-points-to-origin/

## Solution

This question is uses a very similiar technique as "703. Kth Largest Element in a Stream". We will use a priority queue and specifically heapq in python to solve this question in O(nlogk) time.

#### Euclidean Distance

To get the Euclidean Distance from two points it is given by this formula: sqrt((x1 - x2)^2 + (y1 - y2)^2). However, since we are trying to find the k closest points from the origin the formula is simply x^2 + y^2.

#### Maintain Minheap Size k

Now we will utilize the same idea from leetcode "703. Kth Largest Element in a Stream". We will iterate through all of the points and heappush each euclidean distance to our heap. However, if the heap size is ever greater than k, we will simply pop the smallest element so we can maintain the k largest elements. One implementation note is we must push tuples. So, the index of the element AND the euclidean distance. Because when we iterate through the remaining k elements of the heap at the end, we want the coordinates of the k largests points not the euclidean distances.