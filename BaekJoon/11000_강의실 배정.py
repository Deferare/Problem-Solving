from sys import stdin
from collections import deque
import heapq

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]
arr.sort(key=lambda x:x[0])
arr = deque(arr)
tree = []
heapq.heapify(tree)
heapq.heappush(tree, arr.popleft()[1])
while len(arr) > 0:
    dq_pop = arr.popleft()
    tree_pop = heapq.heappop(tree)
    if dq_pop[0] < tree_pop:
        heapq.heappush(tree, dq_pop[1])
        heapq.heappush(tree, tree_pop)
    else:
        heapq.heappush(tree, dq_pop[1])

print(len(tree))
