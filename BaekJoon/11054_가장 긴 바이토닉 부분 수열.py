from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
left_arr = [1 for _ in range(n)]
right_arr = [1 for _ in range(n)]

for i in range(1,n):
    biggest_n = -1
    for j in range(1, i+1):
        if arr[i] > arr[i-j]:
            if left_arr[i-j] > biggest_n:
                biggest_n = left_arr[i-j]
    if biggest_n != -1:
        left_arr[i] = biggest_n+1

for i in range(1,n+1):
    biggest_n = -1
    for j in range(n-i,n):
        if arr[-i] > arr[j]:
            if right_arr[j] > biggest_n:
                biggest_n = right_arr[j]
    if biggest_n != -1:
        right_arr[-i] = biggest_n + 1

result = 0
for i in range(n):
    sum = left_arr[i]+right_arr[i]
    if sum > result:
        result = sum
        
print(result-1)
