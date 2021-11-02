def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        h = len(citations)-i
        if citations[i] >= h:
            return h
    result = 0
    for i in range(len(citations)):
        if citations[i] != 0:
            result = len(citations)-i+1
    return result
