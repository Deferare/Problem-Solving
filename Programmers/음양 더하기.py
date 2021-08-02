def solution(absolutes, signs):
    plus_sum = 0
    minus_sum = 0
    for i in range(len(signs)):
        if signs[i] == True:
            plus_sum += absolutes[i]
        else:
            minus_sum += absolutes[i]
    return plus_sum-minus_sum
