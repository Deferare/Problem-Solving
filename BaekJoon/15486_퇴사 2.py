from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp_arr = [0 for _ in range(n+1)]

for i in range(n):
    if i+arr[i][0] > n:
        if dp_arr[i] < dp_arr[i - 1]:
            dp_arr[i] = dp_arr[i - 1]
        continue
    if dp_arr[i] < dp_arr[i-1]:
        dp_arr[i] = dp_arr[i-1]
    add = arr[i][1] + dp_arr[i]
    if dp_arr[i + arr[i][0]] < add:
        dp_arr[i + arr[i][0]] = add
        
print(max(dp_arr[n], dp_arr[n-1]), end="")
