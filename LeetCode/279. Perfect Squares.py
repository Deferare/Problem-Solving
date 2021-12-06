class Solution:
    def numSquares(self, n: int) -> int:
        sq = []
        dp = []
        for i in range(1, n+1):
            crnt = i**0.5
            if str(crnt)[-1] == "0":
                sq.append(i)
                dp.append(1)
            else:
                min_check = dp[-1]+1
                for j in range(len(sq)):
                    crnt_min = dp[sq[j]-1] + dp[-sq[j]]
                    if crnt_min < min_check:
                        min_check = crnt_min
                dp.append(min_check)
        return dp[-1]
