import heapq
from collections import deque

# O(N) solution
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        q = deque()
        ans = []

        for right_ptr in range(len(nums)):
            # Add value to queue
            while len(q) > 0 and nums[right_ptr] >= nums[q[-1]]:
                q.pop()

            q.append(right_ptr)

            # Max value is in range of window
            while q[0] <= right_ptr - k:
                q.popleft()

            if right_ptr >= k-1:
                ans.append(nums[q[0]])

        return ans

# Slower Solution O(nlogn)
class Solution2:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []

        heap = []
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        left_ptr = 0
        for right_ptr in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[right_ptr], right_ptr))

            max_val = heap[0][0]
            while heap[0][1] < left_ptr:
                heapq.heappop(heap)
                max_val = heap[0][0]

            ans.append(-max_val)
            left_ptr += 1

        return ans
