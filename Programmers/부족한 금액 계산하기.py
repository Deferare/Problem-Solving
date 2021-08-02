def solution(price, money, count):
    answer = 0
    crnt_price = price
    for i in range(count):
        answer += crnt_price
        crnt_price += price
    answer = money - answer
    if answer >= 0:
        answer = 0
    else:
        answer *= -1
    return answer
