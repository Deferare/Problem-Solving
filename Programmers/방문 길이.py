def solution(dirs):
    state_point = [0,0]
    visited = set()
    for order in dirs:
        main_key = str(state_point)
        check = 0
        if order == "U":
            if state_point[0] < 5:
                state_point[0] += 1
                check = 1
        elif order == "R":
            if state_point[1] < 5:
                state_point[1] += 1
                check = 1
        elif order == "D":
            if state_point[0] > -5:
                state_point[0] -= 1
                check = 1
        elif order == "L":
            if state_point[1] > -5:
                state_point[1] -= 1
                check = 1
        if check == 1:
            sub_key = str(state_point)
            key_1 = main_key+sub_key
            key_2 = sub_key+main_key
            if key_1 not in visited and key_2 not in visited:
                visited.add(key_1)
                visited.add(key_2)
    return len(visited)//2
