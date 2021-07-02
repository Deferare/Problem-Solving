from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    n = int(stdin.readline())
    arr_a = list(map(int, stdin.readline().split()))
    arr_b = list(map(int, stdin.readline().split()))
    if n < 3:
        if n == 1:
            print(max(arr_a[0],arr_b[0]))
        elif n == 2:
            print(max(arr_a[0]+arr_b[1], arr_b[0]+arr_b[1]))
    else:
        dp_arr_a = [arr_a[0], arr_b[0] + arr_a[1], 0]
        dp_arr_b = [arr_b[0], arr_a[0] + arr_b[1], 0]
        for i in range(2, n):
            dp_arr_a[2] = max(dp_arr_b[1], dp_arr_b[0]) + arr_a[i]
            dp_arr_b[2] = max(dp_arr_a[1], dp_arr_a[0]) + arr_b[i]
            dp_arr_a[0] = dp_arr_a[1]
            dp_arr_a[1] = dp_arr_a[2]
            dp_arr_b[0] = dp_arr_b[1]
            dp_arr_b[1] = dp_arr_b[2]
        print(max(dp_arr_a[2], dp_arr_b[2]))
