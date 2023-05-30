class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        dp = [0, 1]
        for i in range(2, n, 2):
            dp.append(dp[i // 2])
            dp.append(dp[(i // 2)] + dp[(i // 2) + 1])
        return max(dp)
