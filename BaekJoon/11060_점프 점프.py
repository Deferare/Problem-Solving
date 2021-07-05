from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split(" ")))
memo = [-1 for _ in range(1002)]

def recursion(index):
    if index >= n-1:
        return 0
    if memo[index] != -1:
        return memo[index]
    result = 100002
    for i in range(1, arr[index]+1):
        move = recursion(index+i)
        if move < result:
            result = move
    memo[index] = result + 1
    return memo[index]

result = recursion(0)
if result >= 100002:
    print(-1)
else:
    print(result)
