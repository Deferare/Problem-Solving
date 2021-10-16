import heapq

def solution(scoville, K):
    heap_arr = []
    [heapq.heappush(heap_arr, crnt) for crnt in scoville]
    result_cnt = 0
    while len(heap_arr) > 1:
        pop = heapq.heappop(heap_arr)
        if pop < K:
            heapq.heappush(heap_arr, (heapq.heappop(heap_arr)*2)+pop)
            result_cnt += 1
        else:
            break
    if heapq.heappop(heap_arr) < K:
        return -1
    return result_cnt
