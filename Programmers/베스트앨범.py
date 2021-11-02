def solution(genres, plays):
    note_arr = dict()
    note_sum = dict()
    for i in range(len(genres)):
        if genres[i] not in note_arr:
            note_arr[genres[i]] = [[plays[i], -i]]
            note_sum[genres[i]] = plays[i]
        else:
            note_arr[genres[i]].append([plays[i], -i])
            note_sum[genres[i]] += plays[i]
    note_order = []
    for (key,value) in note_sum.items():
        note_order.append([key, value])
    del note_sum
    note_order.sort(key=lambda x:x[1], reverse=True)
    result = []
    for i in range(len(note_order)):
        note_arr[note_order[i][0]].sort(key=lambda x:(x[0],x[1]), reverse=True)
        for j in range(len(note_arr[note_order[i][0]])):
            result.append(note_arr[note_order[i][0]][j][1] * -1)
            if j == 1:
                break
    return result
