def solution(dartResult):
    main_score = 0
    pre_scores = [0, 0]
    i = 0
    while i < len(dartResult)-1:
        if dartResult[i+1] == "0":
            pre_scores[1] = int(dartResult[i]+dartResult[i+1])
            i += 1
        else:
            pre_scores[1] = int(dartResult[i])
        if dartResult[i+1] == "S":
            pre_scores[1] **= 1
        elif dartResult[i+1] == "D":
            pre_scores[1] **= 2
        elif dartResult[i+1] == "T":
            pre_scores[1] **= 3
        if i+2 < len(dartResult):
            if dartResult[i+2] == "*":
                pre_scores[0] *= 2
                pre_scores[1] *= 2
                i += 1
            elif dartResult[i+2] == "#":
                pre_scores[1] *= -1
                i += 1
        main_score += pre_scores[0]
        pre_scores[0] = pre_scores[1]
        pre_scores[1] = 0
        i += 2
    return main_score + pre_scores[0]
