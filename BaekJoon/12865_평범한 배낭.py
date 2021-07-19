from sys import stdin

n,k = map(int, stdin.readline().split(" "))
items = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]
dp_arr = [0 for _ in range(k+1)]
for i in range(n):
    for j in range(k, 1, -1):
        if items[i][0] <= j:
            dp_arr[j] = max(dp_arr[j], dp_arr[j-items[i][0]] + items[i][1])

print(dp_arr[-1])
