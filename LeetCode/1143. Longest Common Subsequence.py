class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [0 for _ in range(M+1)]
        result = 0
        for i in range(N):
            next_dp = [0]
            for j in range(M):
                if text1[i] == text2[j]:
                    next_dp.append(dp[j] + 1)
                else:
                    next_dp.append(max(next_dp[-1], dp[j+1]))

                if next_dp[-1] > result: result = next_dp[-1]
            dp = next_dp
        return dp[-1]
