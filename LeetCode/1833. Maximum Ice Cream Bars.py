class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        answer = 0
        for i in range(0, len(costs)):
            crnt = costs[i]
            if coins - crnt >= 0:
                coins -= crnt
                answer += 1
            else: break
        return answer
