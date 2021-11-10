from sys import stdin
import heapq
n = int(stdin.readline())
max_arr = []
min_arr = []
heapq.heapify(max_arr)
heapq.heapify(min_arr)

for _ in range(n):
    push_n = int(stdin.readline())
    if len(max_arr) == len(min_arr):
        if len(min_arr) == 0:
            heapq.heappush(max_arr, push_n * -1)
        else:
            min_pop = heapq.heappop(min_arr)
            if push_n > min_pop:
                heapq.heappush(max_arr, min_pop*-1)
                heapq.heappush(min_arr, push_n)
            else:
                heapq.heappush(max_arr, push_n*-1)
                heapq.heappush(min_arr, min_pop)
    else:
        heapq.heappush(min_arr, push_n)
        min_pop = heapq.heappop(min_arr)
        max_pop = heapq.heappop(max_arr)*-1
        if min_pop < max_pop:
            heapq.heappush(max_arr, min_pop*-1)
            heapq.heappush(min_arr, max_pop)
        else:
            heapq.heappush(max_arr, max_pop*-1)
            heapq.heappush(min_arr, min_pop)
    result_pop = heapq.heappop(max_arr)
    heapq.heappush(max_arr, result_pop)
    print(result_pop*-1)
