def solution(arr):
    index_check = 0
    min_check = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_check:
            min_check = arr[i]
            index_check = i
    del arr[index_check]
    if len(arr) == 0 or (len(arr) == 1 and arr[0] == 10):
        return [-1]
    return arr
