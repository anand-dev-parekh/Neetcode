class Solution:
    def trap(self, height: list[int]) -> int:

        l, r = 0, len(height) - 1
        left_max = right_max = 0
        trapped = 0

        while l < r:
            trapped += max(min(left_max, right_max) - height[l], 0)
            trapped += max(min(left_max, right_max) - height[r], 0)

            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if (left_max < right_max):
                l += 1
            else:
                r -= 1

        return trapped
