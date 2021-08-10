# 다시 풀어서 성공.
from sys import stdin

test_case = int(stdin.readline().strip())
for _ in range(test_case):
    n = int(stdin.readline().strip())
    arr = [list(map(int, stdin.readline().split(" "))) for _ in range(2)]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        for i in range(2, n):
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])
        print(max(arr[1][n - 1], arr[0][n - 1]))

# -----------------------예전에 했다가 99% 에서 틀린거.
# from sys import stdin
#
# test_case = int(stdin.readline())
#
# for _ in range(test_case):
#     n = int(stdin.readline())
#     arr_a = list(map(int, stdin.readline().split()))
#     arr_b = list(map(int, stdin.readline().split()))
#     if n < 3:
#         if n == 1:
#             print(max(arr_a[0],arr_b[0]))
#         elif n == 2:
#             print(max(arr_a[0]+arr_b[1], arr_b[0]+arr_b[1]))
#     else:
#         dp_arr_a = [arr_a[0], arr_b[0] + arr_a[1], 0]
#         dp_arr_b = [arr_b[0], arr_a[0] + arr_b[1], 0]
#         for i in range(2, n):
#             dp_arr_a[2] = max(dp_arr_b[1], dp_arr_b[0]) + arr_a[i]
#             dp_arr_b[2] = max(dp_arr_a[1], dp_arr_a[0]) + arr_b[i]
#             dp_arr_a[0] = dp_arr_a[1]
#             dp_arr_a[1] = dp_arr_a[2]
#             dp_arr_b[0] = dp_arr_b[1]
#             dp_arr_b[1] = dp_arr_b[2]
#         print(max(dp_arr_a[2], dp_arr_b[2]))
