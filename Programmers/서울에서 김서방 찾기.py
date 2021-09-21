def solution(seoul):
    index_check = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            index_check = i
            break
    return f"김서방은 {index_check}에 있다"
