from sys import stdin

test_case = int(stdin.readline())
dp_arr = [[0 for _ in range(3)] for _ in range(10000)]
for i in range(3):
    for j in range(i+1):
        dp_arr[i][j] = 1

for i in range(3, 10000):
    dp_arr[i][0] = 1
    dp_arr[i][1] = dp_arr[i-2][0] + dp_arr[i-2][1]
    dp_arr[i][2] = dp_arr[i - 3][0] + dp_arr[i - 3][1] + dp_arr[i - 3][2]

for _ in range(test_case):
    n = int(stdin.readline())
    print(sum(dp_arr[n-1]))
