from collections import deque
def solution(bridge_length2, weight, truck_weights):
    result_cnt = 0
    q = deque()
    trucks = deque(truck_weights)
    recive = 0
    summation = 0
    while recive < len(truck_weights):
        if len(trucks) > 0 and len(q) == 0:
            pop = trucks.popleft()
            q.append(pop)
            summation += pop
            result_cnt += 1
        elif len(trucks) > 0 and len(q) < bridge_length2 and trucks[0] + summation <= weight:
            pop = trucks.popleft()
            q.append(pop)
            summation += pop
            result_cnt += 1
        else:
            if len(q) < bridge_length2:
                q.append(0)
                result_cnt += 1
            else:
                pop = q.popleft()
                if pop != 0:
                    summation -= pop
                    recive += 1
    return result_cnt+1
