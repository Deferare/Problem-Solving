class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_crnt = prices[0]
        max_result = 0
        for i in range(len(prices)):
            cacu = prices[i]-min_crnt
            if cacu > max_result:
                max_result = cacu
            if prices[i] < min_crnt:
                min_crnt = prices[i]
        return max_result
