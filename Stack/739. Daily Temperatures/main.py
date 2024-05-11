from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        ans = [0] * len(temperatures)
        stck = deque()

        for i, t in enumerate(temperatures):

            while len(stck) > 0 and temperatures[stck[0]] < t:
                j = stck.popleft()
                ans[j] = i - j
            
            stck.appendleft(i)

        return ans




