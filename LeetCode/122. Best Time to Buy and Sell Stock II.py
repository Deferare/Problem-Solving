class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        index = 0
        while index+1 < len(prices):
            if prices[index] < prices[index+1]:
                total_profit += (prices[index+1]-prices[index])
            index += 1
        return total_profit
