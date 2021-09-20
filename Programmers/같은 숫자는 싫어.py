def solution(arr):
    visited = set()
    result = []
    pre_value = arr[0]
    for crnt in arr:
        if pre_value != crnt:
            visited.remove(pre_value)
            pre_value = crnt
        if crnt not in visited:
            result.append(crnt)
            visited.add(crnt)
    return result
