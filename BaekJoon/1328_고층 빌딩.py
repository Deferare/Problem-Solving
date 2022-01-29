N, L, R = map(int, input().split(" "))
arr = list(list(list(0 for _ in range(R + 1)) for _ in range(L + 1)) for _ in range(N + 1))
arr[1][1][1] = 1
for i in range(2, N + 1):
    for j in range(1, L + 1):
        for k in range(1, R + 1):
            arr[i][j][k] = (arr[i-1][j-1][k] + arr[i-1][j][k-1] + arr[i-1][j][k] * (i-2))%1000000007
print(arr[N][L][R])
