def solution(priorities, location):
    maxs = []
    for i in range(len(priorities)):
        maxs.append(priorities[i])
        priorities[i] = [i, priorities[i]]
    maxs.sort()
    result_cnt = 0
    while len(priorities) > 0:
        pop = priorities.pop(0)
        if pop[1] == maxs[-1]:
            result_cnt += 1
            if pop[0] == location:
                break
            maxs.pop()
        else:
            priorities.append(pop)
    return result_cnt
