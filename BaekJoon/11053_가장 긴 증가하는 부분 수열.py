from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split(" ")))
memo = [-1 for _ in range(1001)]
def dp(index, status):
    if index < 0:
        return 0
    if memo[index] != -1:
        return memo[index]
    result = -1
    for i in range(1, index+1):
        if arr[index-i] < status:
            save = dp(index-i, arr[index])
            if save > result:
                result = save
    result += 1
    return result
result = 0
for i in range(n):
    if memo[i] == -1:
        save = dp(i, arr[i])
    if save > result:
        result = save
    memo[i] = save
print(result+1)
