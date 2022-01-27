class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0: return 0
        def dp(day, life, state):
            if day >= len(prices) or life == -1: return 0
            if cache[day][life][state] != -1: return cache[day][life][state]
            crnt_day = dp(day + 1, life, state)
            if state:
                crnt_day = max(crnt_day, dp(day + 1, life, 0) - prices[day])
            else:
                crnt_day = max(crnt_day, dp(day + 1, life - 1, 1) + prices[day])
            cache[day][life][state] = crnt_day
            return cache[day][life][state]
        N = len(prices)
        cache = [list(list(-1 for _ in range(2)) for _ in range(k)) for _ in range(N)]
        return dp(0, k - 1, 1)
