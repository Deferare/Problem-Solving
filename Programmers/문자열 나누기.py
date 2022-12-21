def solution(s):
    answer = 0
    startInd = 0
    startCount = 1
    crntInd = 1
    crntCount = 1
    while crntInd < len(s):
        if s[crntInd] == s[startInd]:
            startCount += 1
        else:
            if crntCount == startCount:
                answer += 1
                crntCount, startCount = 0, 0
                startInd = crntInd+1
                crntInd = startInd+1
                continue
            crntCount += 1
        crntInd += 1
    if len(s) == crntInd: answer += 1
    return answer
