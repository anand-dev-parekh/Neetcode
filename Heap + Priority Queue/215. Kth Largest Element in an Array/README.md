# 215. Kth Largest Element in an Array

### Medium

https://leetcode.com/problems/kth-largest-element-in-an-array/

## Solution

The goal of this solution is to find the k-th largest element in an unsorted array. The approach leverages a min-heap to efficiently keep track of the largest elements encountered so far.

#### Idea

A min-heap is a binary heap where the root element is the smallest element in the heap. By maintaining a min-heap of size k, the smallest element in this heap will always be the k-th largest element in the original array.

#### Steps

1. Initialize an empty min-heap: This heap will store the k largest elements as they are encountered in the array.

2. Iterate through each element in the array: For each element, check if the heap has fewer than k elements or if the current element is larger than the smallest element in the heap (the root).

3. Add element to the heap: If either condition is true, push the current element onto the heap.

4. Maintain heap size: If the heap exceeds k elements after adding the new element, remove the smallest element to ensure the heap size remains k.

5. Result: After processing all elements, the smallest element in the heap (the root) will be the k-th largest element in the array.

#### Why This Works

By maintaining a heap of the k largest elements, the solution ensures that all elements in the heap are greater than or equal to the k-th largest element. The k-th largest element will always be at the root of the min-heap. This approach is efficient because heap operations (insertion and deletion) are O(log k), making the overall time complexity O(n log k), where n is the number of elements in the array.