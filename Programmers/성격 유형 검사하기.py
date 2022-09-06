def solution(survey, choices):
    answer = ''

    chart = {
        "RT": [0, 0],
        "TR": [0, 0],
        "FC": [0, 0],
        "CF": [0, 0],
        "MJ": [0, 0],
        "JM": [0, 0],
        "AN": [0, 0],
        "NA": [0, 0],
    }

    chart2 = {
        "RT": [0, 0],
        "CF": [0, 0],
        "JM": [0, 0],
        "AN": [0, 0],
    }

    for i in range(0, choices.__len__()):
        if choices[i] == 1:
            chart[survey[i]][0] += 3
        if choices[i] == 7:
            chart[survey[i]][1] += 3

        if choices[i] == 2:
            chart[survey[i]][0] += 2
        if choices[i] == 6:
            chart[survey[i]][1] += 2

        if choices[i] == 3:
            chart[survey[i]][0] += 1
        if choices[i] == 5:
            chart[survey[i]][1] += 1

    for key in chart.keys():
        ind = 0
        if key[0] == "R" or key[1] == "R":
            if key[1] == "R":
                ind = 1
            chart2["RT"][0] += chart[key][ind]

        ind = 0
        if key[0] == "T" or key[1] == "T":
            if key[1] == "T":
                ind = 1
            chart2["RT"][1] += chart[key][ind]

        ind = 0
        if key[0] == "C" or key[1] == "C":
            if key[1] == "C":
                ind = 1
            chart2["CF"][0] += chart[key][ind]

        ind = 0
        if key[0] == "F" or key[1] == "F":
            if key[1] == "F":
                ind = 1
            chart2["CF"][1] += chart[key][ind]

        ind = 0
        if key[0] == "J" or key[1] == "J":
            if key[1] == "J":
                ind = 1
            chart2["JM"][0] += chart[key][ind]

        ind = 0
        if key[0] == "M" or key[1] == "M":
            if key[1] == "M":
                ind = 1
            chart2["JM"][1] += chart[key][ind]

        ind = 0
        if key[0] == "A" or key[1] == "A":
            if key[1] == "A":
                ind = 1
            chart2["AN"][0] += chart[key][ind]

        ind = 0
        if key[0] == "N" or key[1] == "N":
            if key[1] == "N":
                ind = 1
            chart2["AN"][1] += chart[key][ind]

    for key in chart2:
        if chart2[key][0] > chart2[key][1]:
            answer += key[0]
        elif chart2[key][0] < chart2[key][1]:
            answer += key[1]
        else:
            answer += min(key[0], key[1])
            
    return answer
