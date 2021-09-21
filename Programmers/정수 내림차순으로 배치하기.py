def solution(n):
    arr = [crnt for crnt in str(n)]
    arr.sort(reverse=True)
    result = ""
    for crnt in arr:
        result += crnt
    return int(result)
