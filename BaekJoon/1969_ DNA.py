from sys import stdin
N,M = map(int, stdin.readline().split(" "))
arr = [list(stdin.readline().strip()) for _ in range(N)]
result_cnt = 0
main_strs = [""]
index = 0
while index < M:
    main_strs.sort()
    crnt_strs = [main_strs[0]]
    main_strs.clear()
    max_check = dict()
    max_number = 0
    for i in range(N):
        if arr[i][index] not in max_check:
            max_check[arr[i][index]] = 1
        else:
            max_check[arr[i][index]] += 1
        if max_check[arr[i][index]] > max_number:
            max_number = max_check[arr[i][index]]
    result_cnt += N-max_number
    for (key,value) in max_check.items():
        if value == max_number:
            if index == 0:
                main_strs.append(key)
            else:
                for i in range(len(crnt_strs)):
                    if len(crnt_strs[i]) > 0:
                        main_strs.append(crnt_strs[i] + key)
    index += 1
main_strs.sort()
print(main_strs[0])
print(result_cnt)
