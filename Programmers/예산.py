def solution(d, budget):
    d.sort()
    result_cnt = 0
    _sum = 0
    for crnt in d:
        if _sum+crnt <= budget:
            _sum += crnt
            result_cnt += 1
    return result_cnt
