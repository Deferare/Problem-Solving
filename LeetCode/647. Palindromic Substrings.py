class Solution:
    def countSubstrings(self, s: str) -> int:
        def dp(ind_1, ind_2):
            if ind_1 >= ind_2: return True
            key = f"{ind_1}|{ind_2}"
            if key in memo: return memo[key]
            memo[key] = False
            if s[ind_1] == s[ind_2]:
                memo[key] = dp(ind_1 + 1, ind_2 - 1)
            dp(ind_1 + 1, ind_2)
            dp(ind_1, ind_2 - 1)
            if memo[key] == True:
                result[0] += 1
            return memo[key]
        memo = dict()
        result = [len(s)]
        dp(0, len(s) - 1)
        return result[0]
