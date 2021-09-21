def solution(price, money, count):
    price_accumulate = 0
    for i in range(1, count+1):
        price_accumulate += price*i
    if price_accumulate <= money:
        return 0
    return price_accumulate-money
