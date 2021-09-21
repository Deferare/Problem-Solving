def solution(scores):
    student_len = len(scores)
    result = ""
    for i in range(student_len):
        your_self = scores[i][i]
        min_check = 100
        max_check = 0
        score_acc = 0
        for j in range(student_len):
            if j == i:
                continue
            score_acc += scores[j][i]
            if scores[j][i] > max_check:
                max_check = scores[j][i]
            if scores[j][i] < min_check:
                min_check = scores[j][i]
        if your_self > max_check or your_self < min_check:
            score_sub = score_acc/(student_len-1)
        else:
            score_sub = (score_acc+your_self)/student_len
        if score_sub >= 90:
            result += "A"
        elif score_sub >= 80:
            result += "B"
        elif score_sub >= 70:
            result += "C"
        elif score_sub >= 50:
            result += "D"
        else:
            result += "F"
    return result
