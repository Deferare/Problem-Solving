from sys import stdin
tk = int(stdin.readline())

for _ in range(tk):
    n = int(stdin.readline())
    arr = list(stdin.readline().strip() for _ in range(n))
    arr.sort()
    memo = set()
    memo.add(arr[0])
    check = 0
    for i in range(1, n):
        sub_number = ""
        for j in range(len(arr[i])):
            sub_number += arr[i][j]
            if sub_number in memo:
                check = 1
                break
        if check == 1:
            break
        else:
            memo.add(sub_number)
    if check == 1:
        print("NO")
    else:
        print("YES")
