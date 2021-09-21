def solution(arr, divisor):
    result = []
    for crnt in arr:
        if crnt%divisor == 0:
            result.append(crnt)
    if len(result) == 0:
        result.append(-1)
    else:
        result.sort()
    return result
