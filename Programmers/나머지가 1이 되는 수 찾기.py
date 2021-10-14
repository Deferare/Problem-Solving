def solution(n):
    num = n-1
    div_n = 2
    while div_n < n:
        if num%div_n == 0:
            return div_n
        div_n += 1
    return div_n
