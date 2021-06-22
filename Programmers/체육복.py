def solution(n, lost, reserve):
    dict_lost = {str(lost[i]):1 for i in range(len(lost))}
    dict_reserve = {str(reserve[i]): 1 for i in range(len(reserve))}
    answer = 0
    for i in range(1,n+1):
        if str(i) in dict_lost:
            key1 = str(i)
            if key1 in dict_reserve and dict_reserve[key1] != 0:
                answer += 1
                dict_reserve[key1] = 0
                continue
            key2 = str(i + 1)
            key3 = str(i - 1)
            if key2 in dict_reserve and dict_reserve[key2] != 0 and key2 not in dict_lost:
                dict_reserve[key2] = 0
                answer += 1
            elif key3 in dict_reserve and dict_reserve[key3] != 0 and key3 not in dict_lost:
                dict_reserve[key3] = 0
                answer += 1
        else:
            answer += 1
    return answer
