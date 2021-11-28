import heapq
from collections import deque
class MinStack:
    arr_min = []
    def __init__(self):
        heapq.heapify(self.arr_min)
        self.stack = deque()
        self.info = dict()

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.arr_min, val)
        if val not in self.info:
            self.info[val] = 1
        else:
            self.info[val] += 1

    def pop(self) -> None:
        p = self.stack.pop()
        self.info[p] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        _min = heapq.heappop(self.arr_min)
        while len(self.arr_min) > 0:
            if _min in self.info and self.info[_min] > 0:
                break
            else:
                _min = heapq.heappop(self.arr_min)
        heapq.heappush(self.arr_min, _min)
        return _min
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
