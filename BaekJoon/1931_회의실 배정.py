from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    a,b = map(int, stdin.readline().split())
    arr.append([b,a])

arr.sort()

start_number = arr[0][1]
end_number = arr[0][0]
result_check = 1
for i in range(1, n):
    if arr[i][1] >= end_number and arr[i][0] >= end_number:
        end_number = arr[i][0]
        start_number = arr[i][1]
        result_check += 1
        
print(result_check)
