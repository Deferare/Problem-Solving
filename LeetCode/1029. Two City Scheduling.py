class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        [costs[i].append(costs[i][0]-costs[i][1]) for i in range(len(costs))]
        costs = sorted(costs, key=lambda x:x[2])
        result = 0
        costs_len = int(len(costs)/2)
        for i in range(costs_len):
            result += costs[i][0]
            result += costs[costs_len+i][1]
        return result
