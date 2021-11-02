def solution(progresses, speeds):
    arr = []
    for i in range(len(progresses)):
        a = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] != 0:
            a += 1
        arr.append(a)
    cnt = 1
    pre = arr[0]
    result = []
    for i in range(1,len(arr)):
        if arr[i] > pre:
            pre = arr[i]
            result.append(cnt)
            cnt = 0
        cnt += 1
    result.append(cnt)
    return result
