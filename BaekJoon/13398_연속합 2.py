n = int(input())
arr = list(map(int, input().split(" ")))

dp_arr_1 = [arr[0], 0]
dp_arr_2 = [arr[0], 0]
result_max = arr[0]
for i in range(1, n):
    dp_arr_1[1] = max(dp_arr_1[0]+arr[i], arr[i])
    dp_arr_2[1] = max(dp_arr_1[0], dp_arr_2[0]+arr[i])
    if dp_arr_1[1] > result_max:
        result_max = dp_arr_1[1]
    if dp_arr_2[1] > result_max:
        result_max = dp_arr_2[1]
    dp_arr_1[0] = dp_arr_1[1]
    dp_arr_2[0] = dp_arr_2[1]

print(result_max)
