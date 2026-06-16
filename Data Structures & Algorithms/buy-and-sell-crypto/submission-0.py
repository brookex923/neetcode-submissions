class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for buy in range(0, len(prices) -1):
            for sell in range(buy, len(prices)):
                profit = max(prices[sell] - prices[buy], profit)

        return profit



