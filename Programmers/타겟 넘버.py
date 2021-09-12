def solution(numbers, target):
    first_arr = [numbers[0], -numbers[0]]
    for i in range(1, len(numbers)):
        second_arr = []
        for crnt in first_arr:
            second_arr.append(crnt+numbers[i])
            second_arr.append(crnt-numbers[i])
        first_arr = second_arr.copy()
    result_cnt = 0
    for crnt in first_arr:
        if crnt == target:
            result_cnt += 1
    return result_cnt
