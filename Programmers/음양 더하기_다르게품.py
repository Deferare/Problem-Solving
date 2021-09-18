def solution(absolutes, signs):
    result_sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            result_sum += absolutes[i]
        else:
            result_sum -= absolutes[i]
    return result_sum
