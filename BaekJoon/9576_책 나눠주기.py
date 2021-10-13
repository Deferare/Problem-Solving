from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    n,m = map(int, stdin.readline().split(" "))
    books = [1 for _ in range(n+1)]
    arr = [list(map(int, stdin.readline().split(" "))) for _ in range(m)]
    arr.sort(key=lambda x:x[1])
    result_cnt = 0
    for i in range(m):
        if arr[i][0] > n:
            break
        for j in range(arr[i][0], arr[i][1]+1):
            if j > n:
                break
            if books[j] == 1:
                books[j] = 0
                result_cnt += 1
                break
    print(result_cnt)
