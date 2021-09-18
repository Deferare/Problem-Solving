def solution(array, commands):
    result_cnt = []
    for crnt in commands:
        sub_arr = [array[i] for i in range(crnt[0]-1, crnt[1])]
        sub_arr.sort()
        result_cnt.append(sub_arr[crnt[2]-1])
    return result_cnt
