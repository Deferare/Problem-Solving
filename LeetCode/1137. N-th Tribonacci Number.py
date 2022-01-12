from collections import deque
class Solution:
    def tribonacci(self, n: int) -> int:
        arr = deque([0 ,1, 1])
        if n < 3: return arr[n]
        for _ in range(3, n + 1):
            tmp = sum(arr)
            arr.popleft()
            arr.append(tmp)
        return arr[-1]
