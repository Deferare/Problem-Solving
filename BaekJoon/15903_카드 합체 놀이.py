import heapq
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
heapq.heapify(arr)
for _ in range(M):
    a = heapq.heappop(arr)
    a += heapq.heappop(arr)
    heapq.heappush(arr, a)
    heapq.heappush(arr, a)
print(sum(arr))
