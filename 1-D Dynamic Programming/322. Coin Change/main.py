class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [100000] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):

            for coin in coins:
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != 100000 else -1