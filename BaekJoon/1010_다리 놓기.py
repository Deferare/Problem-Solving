from sys import stdin

test_case = int(stdin.readline())
dp_arr = [[i for i in range(1,31)]]
for i in range(1, 31):
    sub_arr = [0 for _ in range(i)]
    for j in range(i, 31):
        sub_arr.append(dp_arr[i-1][j-1]+sub_arr[j-1])
    dp_arr.append(sub_arr)

for _ in range(test_case):
    n,m = map(int, stdin.readline().split(" "))
    print(dp_arr[n-1][m-1])
