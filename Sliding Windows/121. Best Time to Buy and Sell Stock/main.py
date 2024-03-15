class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_profit = 0
        min_buy = 10000

        for num in prices:
            max_profit = max(num - min_buy, max_profit)
            min_buy = min(num, min_buy)

        return max_profit
