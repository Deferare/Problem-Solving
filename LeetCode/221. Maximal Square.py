class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N, M = len(matrix), len(matrix[0])
        dp = [0 for _ in range(M + 1)]
        result = 0
        prev = 0
        for i in range(N):
            for j in range(M):
                tmp = dp[j + 1]
                if matrix[i][j] == "0":
                    dp[j + 1] = 0
                else:
                    dp[j + 1] = min(prev, dp[j], dp[j + 1]) + 1
                prev = tmp
            result = max(result, *dp)
        return result * result
