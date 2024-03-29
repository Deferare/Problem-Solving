class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            max_value = arr[i]
            for j in range(1, min(k, i+1)+1):
                max_value = max(max_value, arr[i-j+1])
                dp[i] = max(dp[i], (dp[i-j] + max_value * j))
        return dp[-2]
