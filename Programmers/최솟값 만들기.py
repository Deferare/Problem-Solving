def solution(A,B):
    A.sort(reverse=True)
    B.sort(reverse=False)
    result_sum = 0
    for i in range(len(A)):
        result_sum += A[i]*B[i]
    return result_sum
