import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for n in stones:
            arr.append(n*-1)
        heapq.heapify(arr)
        while len(arr) > 1:
            a = heapq.heappop(arr)*-1
            b = heapq.heappop(arr)*-1
            y = a-b
            if y > 0:
                heapq.heappush(arr, -y)
        if len(arr) == 0: return 0
        if arr[0] < 0: arr[0] *= -1
        return arr[0]
