def solution(x):
    x_sum = 0
    for n in str(x):
        x_sum += int(n)
    if x%x_sum != 0:
        return False
    return True
