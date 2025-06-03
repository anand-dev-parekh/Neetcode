class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        partition_sum = total_sum // 2

        dp = [False] * (partition_sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(partition_sum, num-1, -1):
                dp[i] = dp[i-num] or dp[i]

        return dp[-1]
