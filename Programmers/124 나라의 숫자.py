def solution(n):
    result = ""
    while n > 0:
        if n%3 == 0:
            result = "4"+result
            n -= 1
        elif n%3 == 1:
            result = "1"+result
        else:
            result = "2"+result
        n //= 3
    return result
