# 1046. Last Stone Weight

### Easy

https://leetcode.com/problems/last-stone-weight/description/

## Solution

The intuitive idea behind this question is sort the array and extract the two minimum values and push the differece between these two values. However, this is a O(n^2) and can be improved upon by using a priority queue. We will use a heapq in python. 

The first thing we can do is heapify the stones array, which is an O(nlogn) process. We can simulate the rock smashing by using a while loop with the condition of len(stones) > 1. In each iteration we can pop the two largest elements and append the difference of the largest stones (only if the difference != 0). After we exit the array, we simply return the first and only element of the array if it exists else 0 meaning all rocks were destroyed in the process.

#### Implementation Note

One detail to note when using heapq in python is that it is a minheap. However in this question we want to use a maxheap to get the largest stone in logn time. To do this we multiply every element in the stones array by -1. Thus the largest element will now be the smallest and will be popped with the minheap.