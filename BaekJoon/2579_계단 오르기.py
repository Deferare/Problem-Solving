stairs_num = int(input())
stairs = [int(input()) for _ in range(stairs_num)]
memo = [-1 for _ in range(stairs_num)]

def dp(index):
    if index == 0:
        return stairs[0]
    if index < 0:
        return 0
    if memo[index] != -1:
        return memo[index]
    memo[index] = max(dp(index-3) + stairs[index-1], dp(index-2)) + stairs[index]
    return memo[index]

print(dp(stairs_num-1))
