def solution(left, right):
    result_sum = 0
    for n in range(left,right+1):
        result_divisor = []
        for i in range(1, (n // 2) + 1):
            if n%i == 0:
                result_divisor.append(i)
        result_divisor.append(n)
        if len(result_divisor)%2 == 0:
            result_sum += n
        else:
            result_sum -= n
    return result_sum
