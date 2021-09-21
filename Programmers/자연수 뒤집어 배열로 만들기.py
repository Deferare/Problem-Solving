def solution(n):
    n_trans = str(n)
    result_arr = []
    for i in range(1, len(n_trans)+1):
        result_arr.append(int(n_trans[-i]))
    return result_arr
