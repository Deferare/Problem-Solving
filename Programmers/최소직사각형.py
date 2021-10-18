def solution(sizes):
    w_check = 0
    h_check = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            w_check = max(w_check,sizes[i][0])
            h_check = max(h_check,sizes[i][1])
        else:
            w_check = max(w_check,sizes[i][1])
            h_check = max(h_check,sizes[i][0])
    return w_check*h_check
