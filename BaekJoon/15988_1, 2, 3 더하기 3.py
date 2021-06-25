from sys import stdin

test_case = int(stdin.readline())
dp_arr = [[0 for _ in range(3)] for _ in range(3)]
dp_arr[0][0], dp_arr[1][0], dp_arr[1][1] = 1,1,1
dp_arr[2][0], dp_arr[2][1], dp_arr[2][2] = 2,1,1
for i in range(3,1000001):
    a = sum(dp_arr[i - 1])%1000000009
    b = sum(dp_arr[i - 2])%1000000009
    c = sum(dp_arr[i - 3])%1000000009
    dp_arr.append([a,b,c])
for j in range(test_case):
    n = int(stdin.readline())
    print(sum(dp_arr[n-1])%1000000009)
