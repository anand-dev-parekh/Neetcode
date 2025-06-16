class Solution:
    def canJump(self, nums: list[int]) -> bool:

        max_jump_i = 0
        for i, num in enumerate(nums):
            if i > max_jump_i:
                return False

            max_jump_i = max(max_jump_i, i + num)

        return max_jump_i >= len(nums) - 1
