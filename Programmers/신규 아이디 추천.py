def solution(new_id):
    result_id = []
    for i in range(len(new_id)):
        if new_id[i] == "-" or new_id[i] == "_" or new_id[i] == ".":
            result_id.append(new_id[i])
        else:
            asci_value = ord(new_id[i])
            if asci_value >= 65 and asci_value <= 90:
                result_id.append(chr(asci_value + 32))
            elif asci_value >= 97 and asci_value <= 122 or asci_value >= 48 and asci_value <= 57:
                result_id.append(new_id[i])

    next_result = []
    i = 0
    while i < len(result_id):
        if result_id[i] == ".":
            if i + 1 < len(result_id) and result_id[i + 1] == ".":
                for j in range(i, len(result_id)):
                    if result_id[j] != "." or j == len(result_id) - 1:
                        i = j-1
                        break
                next_result.append(".")
            else:
                next_result.append(".")
        else:
            next_result.append(result_id[i])
        i += 1
    while len(next_result) > 0 and next_result[0] == ".":
        next_result.pop(0)
    while len(next_result) > 0 and next_result[-1] == ".":
        next_result.pop(-1)
    if len(next_result) == 0:
        next_result.append("a")
    elif len(next_result) > 15:
        next_result = next_result[:15]
        if next_result[14] == ".":
            del next_result[14]
    if len(next_result) <= 2:
        if len(next_result) <= 2:
            sub_ = next_result[-1]
            for _ in range(len(next_result), 3):
                next_result.append(sub_)
    result = ""
    for crnt in next_result:
        result += crnt
    return result
