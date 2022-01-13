from collections import deque
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = deque([0, 1, 2])
        if n < 3: return arr[n]
        for _ in range(3, n + 1):
            arr.append(arr[-1] + arr[-2])
            arr.popleft()
        return arr[-1]
