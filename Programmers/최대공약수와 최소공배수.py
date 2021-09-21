import math
def solution(n, m):
    least = math.gcd(n, m)
    greatest = (n*m)//least
    answer = [least, greatest]
    return answer
