def solution(weights, head2head):
    players_data = []
    for i in range(len(weights)):
        sub_data = [i+1, weights[i]]
        w = 0; l = 0; n = 0
        critical = 0
        for j in range(len(head2head)):
            if head2head[i][j] == "W":
                w += 1
                if weights[i] < weights[j]:
                    critical += 1
            elif head2head[i][j] == "L":
                l += 1
            else:
                n += 1
        if w != 0:
            sub_data.append(w/(l+w))
        else:
            sub_data.append(0)
        sub_data.append(critical)
        players_data.append(sub_data)
    players_data_1 = sorted(players_data, key=lambda x:(x[2], x[3], x[1]), reverse=True)

    result_arr = [players_data_1[i][0] for i in range(len(players_data_1))]
    return result_arr
