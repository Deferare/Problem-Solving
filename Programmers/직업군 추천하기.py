def solution(table, languages, preference):
    table = list(list(map(str, crnt.split(" "))) for crnt in table)
    occupation_score = []
    lagua_score = dict()
    for i in range(len(languages)):
        lagua_score[languages[i]] = preference[i]
    for i in range(len(table)):
        sub_result = [table[i][0], 0]
        for j in range(1, len(table[i])):
            if table[i][j] in languages:
                sub_result[1] += (lagua_score[table[i][j]] * (len(table[i])-j))
        occupation_score.append(sub_result)
    occupation_score = sorted(occupation_score, key=lambda x:(x[1], x[0]), reverse=True)
    for i in range(len(occupation_score)):
        if i == len(occupation_score)-1 or occupation_score[i][1] != occupation_score[i+1][1]:
            return occupation_score[i][0]
    return occupation_score[0][0]
