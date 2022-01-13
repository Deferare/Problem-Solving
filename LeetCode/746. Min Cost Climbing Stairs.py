class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(index):
            if index < 0: return 0
            elif index == 0: return cost[0]
            elif index == 1: return cost[1]
            if index in memo: return memo[index]
            memo[index] = min(dp(index - 1), dp(index - 2)) + cost[index]
            return memo[index]
        memo = dict()
        result = min(dp(len(cost) - 1), dp(len(cost) - 2))
        return result
