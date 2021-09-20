def solution(N, stages):
    people_n = len(stages)
    stages_difficutlty = []
    stages_people = []
    for i in range(N+1):
        stages_people.append(0)
        stages_difficutlty.append([i, 0])
    for i in range(people_n):
        if stages[i] <= N:
            stages_people[stages[i]] += 1
    for i in range(1, N+1):
        if stages_people[i] == 0:
            stages_difficutlty[i][1] = 0
        else:
            stages_difficutlty[i][1] = stages_people[i]/people_n
            people_n -= stages_people[i]
    stages_difficutlty = sorted(stages_difficutlty, key=lambda x:x[1], reverse=True)
    result = []
    for crnt in stages_difficutlty:
        if crnt[0] != 0:
            result.append(crnt[0])
    return result
