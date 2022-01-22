from sys import stdin
for _ in range(int(stdin.readline())):
    C = int(stdin.readline())
    coins = list(map(int, stdin.readline().split(" ")))
    target = int(stdin.readline())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for i in range(C):
        coin = coins[i]
        while coin <= target:
            dp[coin] += dp[coin-coins[i]]
            coin += 1
    print(dp[-1])
