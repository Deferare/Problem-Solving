def solution(participant, completion):
    completion_dict = {}
    for crnt in completion:
        if crnt in completion_dict:
            completion_dict[crnt] += 1
        else:
            completion_dict[crnt] = 1
    answer = ""
    for crnt in participant:
        if crnt in completion_dict:
            if completion_dict[crnt] == 0:
                answer = crnt
                break
            else:
                completion_dict[crnt] -= 1
        if crnt not in completion_dict:
            answer = crnt
            break

    return answer
