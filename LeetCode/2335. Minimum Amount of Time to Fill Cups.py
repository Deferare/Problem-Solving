import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        new_amount = []
        for v in amount: new_amount.append(-v)
        heapq.heapify(new_amount)
        answer = 0
        while len(new_amount) > 0:
            pop_1 = heapq.heappop(new_amount)
            if len(new_amount) > 0:
                pop_2 = heapq.heappop(new_amount)
                if pop_2 != 0: heapq.heappush(new_amount, pop_2+1)
            if pop_1 != 0: heapq.heappush(new_amount, pop_1+1)
            if pop_1 != 0 or pop_2 != 0:
                answer += 1
        return answer
