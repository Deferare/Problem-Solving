def solution(record):
    reco_arr = []
    info = dict()
    for crnt in record:
        crnt = list(map(str, crnt.split(" ")))
        if crnt[0][0] == "E":
            reco_arr.append([crnt[0], crnt[1]])
            info[crnt[1]] = crnt[2]
        elif crnt[0][0] == "L":
            reco_arr.append([crnt[0], crnt[1]])
        elif crnt[0][0] == "C":
            info[crnt[1]] = crnt[2]
    for i in range(len(reco_arr)):
        if reco_arr[i][0][0] == "E":
            reco_arr[i] = f"{info[reco_arr[i][1]]}님이 들어왔습니다."
        elif reco_arr[i][0][0] == "L":
            reco_arr[i] = f"{info[reco_arr[i][1]]}님이 나갔습니다."
    return reco_arr
