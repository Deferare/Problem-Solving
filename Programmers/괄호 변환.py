def validCheck(bracket_sub):
    cnt = 0
    for i in range(len(bracket_sub)):
        if bracket_sub[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt != 0:
        return False
    return True

def balanceSplit(bracket_sub):
    cnt = 0
    for i in range(len(bracket_sub)):
        if bracket_sub[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def recursion(sub_p):
    if validCheck(sub_p):
        return sub_p
    index = balanceSplit(sub_p)
    u = sub_p[:index+1];
    if index+1 == len(sub_p):
        v = ""
    else:
        v = sub_p[index+1:]
    if validCheck(u):
        if len(v) > 0:
            u += recursion(v)
    else:
        if len(v) > 0:
            sub = "(" + recursion(v) + ")"
        else:
            sub = "()"
        for i in range(1, len(u)-1):
            if u[i] == "(":
                sub += ")"
            else:
                sub += "("
        return sub
    return u

def solution(p):
    return recursion(p)
