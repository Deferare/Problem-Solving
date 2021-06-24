from sys import stdin

test_case = int(input())
dp_arr = []

for _ in range(test_case):
    n = int(stdin.readline())
    if n < 3:
        print(1)
    elif n == 3:
        print(3)
    else:
        if len(dp_arr) == 0:
            dp_arr = [[0 for _ in range(3)] for _ in range(100001)]
            dp_arr[0][0] = 1
            dp_arr[1][1] = 1
            dp_arr[2][0] = 1
            dp_arr[2][1] = 1
            dp_arr[2][2] = 1
            for i in range(3, 100001):
                dp_arr[i][0] = (dp_arr[i - 1][1] + dp_arr[i - 1][2]) % 1000000009
                dp_arr[i][1] = (dp_arr[i - 2][0] + dp_arr[i - 2][2]) % 1000000009
                dp_arr[i][2] = (dp_arr[i - 3][0] + dp_arr[i - 3][1]) % 1000000009
        print(sum(dp_arr[n - 1]) % 1000000009)
