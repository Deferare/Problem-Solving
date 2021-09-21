import math
def solution(n):
    number = math.sqrt(n)
    if str(number)[-1] != "0":
        return -1
    return int((number+1)**2)
