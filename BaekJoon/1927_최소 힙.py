from sys import stdin
import heapq
n = int(stdin.readline())
arr = []
heapq.heapify(arr)
for _ in range(n):
    p = int(stdin.readline())
    if p == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, p)
