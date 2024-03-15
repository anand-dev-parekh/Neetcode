class Solution:
    def maxArea(self, height: list[int]) -> int:

        l, r = 0, len(height) - 1
        ans = min(height[l], height[r]) * max(r-l, 1)

        while l < r:

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

            ans = max(ans, min(height[l], height[r]) * (r-l))
        return ans
