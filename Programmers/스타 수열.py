def solution(a):
    numbers = dict()
    for crnt in a:
        if crnt not in numbers:
            numbers[crnt] = 1
        else:
            numbers[crnt] += 1
    sort_arr = []
    for key,value in numbers.items():
        sort_arr.append([key, value])
    sort_arr = sorted(sort_arr, key=lambda x:x[1], reverse=True)
    max_check = 0
    for crnt in sort_arr:
        if crnt[1]*2 <= max_check:
            break
        pre_index = -1
        sub_max = 0
        i = 0
        while i < len(a):
            if a[i] == crnt[0]:
                if i != 0 and a[i] != a[i-1] and i-1 != pre_index:
                    sub_max += 2
                    pre_index = i
                elif i != len(a)-1 and a[i] != a[i+1]:
                    sub_max += 2
                    pre_index = i+1
            i += 1
        if sub_max > max_check:
            max_check = sub_max
        if max_check == len(a):
            break
    return max_check
