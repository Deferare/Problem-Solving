class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        result = 0
        sub_max = cost[0]
        for i in range(1, len(cost)):
            if s[i] == s[i-1]:
                if cost[i] > sub_max:
                    result += sub_max
                    sub_max = cost[i]
                elif cost[i] <= sub_max:
                    result += cost[i]
            if s[i] != s[i-1]:
                sub_max = cost[i]
        return result
