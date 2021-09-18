def solution(participant, completion):
    participant_dict = dict()
    for crnt in participant:
        if crnt not in participant_dict:
            participant_dict[crnt] = 1
        else:
            participant_dict[crnt] += 1
    for crnt in completion:
        if crnt in participant_dict:
            participant_dict[crnt] -= 1
            if participant_dict[crnt] == 0:
                del participant_dict[crnt]
        else:
            return crnt
    return participant_dict.popitem()[0]
