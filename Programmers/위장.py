def solution(clothes):
    closet = dict()
    for i in range(len(clothes)):
        if clothes[i][1] not in closet:
            closet[clothes[i][1]] = 1
        else:
            closet[clothes[i][1]] += 1
    result = 0
    for value in closet.values():
        result += result*value
        result += value
    return result
