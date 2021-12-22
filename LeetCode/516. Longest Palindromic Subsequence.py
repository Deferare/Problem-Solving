class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dp(index_1, index_2):
            if index_1 == index_2:
                return 1
            elif index_1 > index_2:
                return 0

            if memo[index_1][index_2] != -1:
                return memo[index_1][index_2]
            if s[index_1] == s[index_2]:
                memo[index_1][index_2] = dp(index_1+1, index_2-1) + 2
            else:
                memo[index_1][index_2] = max(dp(index_1+1, index_2), dp(index_1, index_2-1))
            return memo[index_1][index_2]
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        result = dp(0, len(s) - 1)
        return result
