def solution(lottos, win_nums):
    win_set = set(win_nums)
    zero_cnt = 0
    right_cnt = 0
    for crnt in lottos:
        if crnt == 0:
            zero_cnt += 1
        else:
            if crnt in win_set:
                right_cnt += 1
    win_result = 7-right_cnt-zero_cnt
    if win_result > 6:
        win_result = 6
    loss_result = (win_result)+(zero_cnt)
    if loss_result > 6:
        loss_result -= 1
    answer = [win_result, loss_result]
    return answer
