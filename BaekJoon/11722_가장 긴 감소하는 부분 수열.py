from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp_arr = [1 for _ in range(n)]

for i in range(2, n+1):
    biggest_n = -1
    for j in range(n-i+1, n):
        if arr[-i] > arr[j] and dp_arr[j] > biggest_n:
            dp_arr[-i] = dp_arr[j] + 1
            biggest_n = dp_arr[j]
            
print(max(dp_arr))
