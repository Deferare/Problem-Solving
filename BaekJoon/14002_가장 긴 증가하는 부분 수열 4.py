n = int(input())
arr = list(map(int, input().split(" ")))
arr_save = [[arr[0]]]
for i in range(1, n):
    check = 0
    len_max = 0
    len_index = 0
    for j in range(i):
        if arr[i] > arr[j]:
            sub_len = len(arr_save[j])
            if sub_len > len_max:
                len_max = sub_len
                len_index = j
                check = 1
    if check == 1:
        push_arr = arr_save[len_index].copy()
        push_arr.append(arr[i])
        arr_save.append(push_arr)
    else:
        arr_save.append([arr[i]])

result_index = 0
result_max = 0
for i in range(n):
    sub_len = len(arr_save[i])
    if sub_len > result_max:
        result_max = sub_len
        result_index = i
        
print(result_max)
print(*arr_save[result_index])
