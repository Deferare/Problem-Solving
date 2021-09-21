def solution(s):
    s = list(s)
    s.sort(reverse=True)
    answer = ""
    for crnt in s:
        answer += crnt
    return answer
