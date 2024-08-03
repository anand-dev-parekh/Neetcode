class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [0] * len(nums)


        for i, num in enumerate(nums):
            for j in range(i-1, -1, -1):
                if nums[j] < num:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp) + 1