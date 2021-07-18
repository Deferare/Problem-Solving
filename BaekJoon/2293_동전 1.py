from sys import stdin

n,m = map(int, stdin.readline().split(" "))
coin = [int(stdin.readline()) for _ in range(n)]

dp_arr = [0 for _ in range(m+1)]
dp_arr[0] = 1
for i in range(n):
    for j in range(coin[i], m+1):
        dp_arr[j] += dp_arr[j-coin[i]]
        
print(dp_arr[m])
