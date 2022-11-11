class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        answer = 0
        ind = 0
        while ind < len(cost):
            answer += cost[ind]
            if ind+1 < len(cost):
                answer += cost[ind+1]
                ind += 1
            ind += 2
        return answer
