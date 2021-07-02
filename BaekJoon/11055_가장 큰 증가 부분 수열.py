from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
sum_arr = arr.copy()

for i in range(1, n):
    sum = -1
    for j in range(i):
        if arr[j] < arr[i]:
            sub = sum_arr[j] + arr[i]
            if sub > sum:
                sum = sub
    if sum != -1:
        sum_arr[i] = sum

print(max(sum_arr))
