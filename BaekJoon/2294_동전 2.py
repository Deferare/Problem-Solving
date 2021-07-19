from sys import stdin

n,k = map(int, stdin.readline().split(" "))
coins = [int(stdin.readline()) for _ in range(n)]
dp_arr = [0 for _ in range(k+1)]
for coin in coins:
    for j in range(coin, k+1):
        if coin == j:
            dp_arr[j] = 1
        else:
            if dp_arr[j] == 0 and dp_arr[j-coin] == 0:
                dp_arr[j] = 0
            elif dp_arr[j] != 0 and dp_arr[j-coin] != 0:
                dp_arr[j] = min(dp_arr[j - coin] + 1, dp_arr[j])
            else:
                if dp_arr[j] == 0:
                    dp_arr[j] = dp_arr[j-coin]+1

if dp_arr[k] == 0:
    print(-1)
else:
    print(dp_arr[k])
