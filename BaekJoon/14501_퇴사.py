n = int(input())
time = [0 for _ in range(n)]
money = [0 for _ in range(n)]
for i in range(n):
    save = list(map(int, input().split(" ")))
    time[i] = save[0]
    money[i] = save[1]

def dp(now_index):
    if now_index > n-1:
        return 0
    if time[now_index] > n-now_index:
        return dp(now_index+1)
    return max(dp(now_index+time[now_index])+money[now_index], dp(now_index+1))
print(dp(0))
