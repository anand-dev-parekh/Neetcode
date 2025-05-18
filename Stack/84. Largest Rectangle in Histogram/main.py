class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []
        max_area = 0
        for i, height in enumerate(heights):

            j = i
            while stack and stack[-1][0] >= height:
                height_j, j = stack.pop()
                max_area = max((i - j) * height_j, max_area)

            stack.append((height, j))

        for h, i in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
