class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        res = 0
        for i, num in enumerate(nums):
            res ^= num ^ i

        return res ^ len(nums)
