def solution(n, lost, reserve):
    lost.sort(); reserve.sort()
    arr = [1 for _ in range(n)]
    reserve_set = set(reserve)
    for i in range(len(lost)):
        if lost[i] in reserve_set:
            reserve_set.remove(lost[i])
        else:
            arr[lost[i]-1] = 0
    for i in range(len(reserve)):
        if reserve[i] in reserve_set:
            if reserve[i] > 1 and arr[reserve[i]-2] == 0:
                arr[reserve[i]-2] = 1
            elif reserve[i] < n and arr[reserve[i]] == 0:
                arr[reserve[i]] = 1
    return sum(arr)
