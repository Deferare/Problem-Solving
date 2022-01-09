import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k_ = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k_:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k_: heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
