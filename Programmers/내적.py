def solution(a, b):
    result_sum = 0
    for i in range(len(a)):
        result_sum += a[i]*b[i]
    return result_sum
