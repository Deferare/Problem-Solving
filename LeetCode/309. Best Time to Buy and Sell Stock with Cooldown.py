class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(day, state):
            if day >= N: return 0
            if cache[day][state] != -1: return cache[day][state]
            crnt = dp(day + 1, state)
            if state == 1:
                crnt = max(crnt, dp(day + 1, 0) - prices[day])
            elif state == 0:
                crnt = max(crnt, dp(day + 2, 1) + prices[day])
            cache[day][state] = crnt
            return crnt
        N = len(prices)
        cache = [list(-1 for _ in range(2)) for _ in range(N)]
        return dp(0, 1)
