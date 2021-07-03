from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    n = int(stdin.readline())
    arr = [[] for _ in range(n)]
    for _ in range(n):
        put = list(map(int, stdin.readline().split()))
        arr[put[0]-1] = put

    save_max = arr[0][1]
    result_check = 1

    for i in range(1, n):
        if arr[i][1] > save_max:
            pass
        else:
            save_max = arr[i][1]
            result_check += 1
            
    print(result_check)
