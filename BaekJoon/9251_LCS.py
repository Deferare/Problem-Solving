arr_1 = input()
arr_2 = input()
lenght = max(len(arr_1), len(arr_2))
dp_arr = [[0 for _ in range(lenght+1)] for _ in range(lenght+1)]

for i in range(len(arr_2)):
    for j in range(len(arr_1)):
        if arr_1[j] == arr_2[i]:
            dp_arr[i+1][j+1] = dp_arr[i][j] + 1
        else:
            dp_arr[i+1][j+1] = max(dp_arr[i][j+1], dp_arr[i+1][j])
print(dp_arr[len(arr_2)][len(arr_1)])
