from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]
dp_arr = [[0 for _ in range(n)] for _ in range(n)]
dp_arr[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        sub_value = arr[i][j]
        if i + sub_value < n:
            dp_arr[i + sub_value][j] += dp_arr[i][j]
        if j + sub_value < n:
            dp_arr[i][j + sub_value] += dp_arr[i][j]

print(dp_arr[n-1][n-1])
