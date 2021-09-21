def solution(s):
    cnt = 0
    for crnt in s:
        if crnt == "p" or crnt == "P":
            cnt += 1
        elif crnt == "y" or crnt == "Y":
            cnt -= 1
    if cnt != 0:
        return False
    return True
