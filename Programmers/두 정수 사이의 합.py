def solution(a, b):
    result_sum = 0
    if a > b:
        tmp = a
        a = b
        b = tmp
    for crnt in range(a,b+1):
        result_sum += crnt
    return result_sum
