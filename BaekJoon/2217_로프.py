from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
arr.sort()

result_max = -1

for i in range(1, n+1):
    sub = arr[-i] * i
    if sub > result_max:
        result_max = sub

print(result_max)
