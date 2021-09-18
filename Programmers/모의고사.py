def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_ = 0; b_ = 0; c_ = 0
    index_1 = 0; index_2 = 0; index_3 = 0;
    for i in range(len(answers)):
        if a[index_1] == answers[i]:
            a_ += 1
        if b[index_2] == answers[i]:
            b_ += 1
        if c[index_3] == answers[i]:
            c_ += 1
        index_1 += 1; index_2 += 1; index_3 += 1
        if (index_1)%5 == 0:
            index_1 = 0
        if (index_2)%8 == 0:
            index_2 = 0
        if (index_3)%10 == 0:
            index_3 = 0
    result_arr = [a_, b_, c_]
    if result_arr[0] == result_arr[1] and result_arr[1] == result_arr[2]:
        return [1,2,3]
    elif result_arr[0] > result_arr[1] and result_arr[0] > result_arr[2]:
        return [1]
    elif result_arr[1] > result_arr[0] and result_arr[1] > result_arr[2]:
        return [2]
    elif result_arr[2] > result_arr[0] and result_arr[2] > result_arr[1]:
        return [3]
    elif result_arr[0] == result_arr[1]:
        return [1, 2]
    elif result_arr[0] == result_arr[2]:
        return [1, 3]
    elif result_arr[1] == result_arr[2]:
        return [2, 3]
    return result_arr
