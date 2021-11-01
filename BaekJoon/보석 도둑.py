from sys import stdin
from collections import deque
import heapq

n, bag_n = map(int, stdin.readline().split(" "))
jewelrys = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]
bags = [int(stdin.readline()) for _ in range(bag_n)]

jewelrys.sort(key=lambda x:x[0])
bags.sort()

jewelrys = deque(jewelrys)
result = 0
arr = []
heapq.heapify(arr)
for i in range(len(bags)):
    while len(jewelrys) > 0:
        pop = jewelrys.popleft()
        if bags[i] >= pop[0]:
            heapq.heappush(arr, -pop[1])
        else:
            jewelrys.appendleft(pop)
            break
    if len(arr) > 0:
        result += heapq.heappop(arr)

print(result*-1)
