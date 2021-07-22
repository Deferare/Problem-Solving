from sys import stdin
import heapq

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
heapq.heapify(arr)
result = 0
while 1 < len(arr):
    sub = heapq.heappop(arr)
    sub += heapq.heappop(arr)
    result += sub
    heapq.heappush(arr, sub)
print(result)
