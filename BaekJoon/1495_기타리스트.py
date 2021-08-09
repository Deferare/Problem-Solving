n,s,m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
dp_arr = [0 for _ in range(m+1)]
pre_arr = [s]
check = 0
for i in range(n):
    second_set = set()
    for crnt in pre_arr:
        if crnt+arr[i] <= m:
            if crnt+arr[i] not in second_set:
                second_set.update([crnt+arr[i]])
        if crnt-arr[i] >= 0:
            if crnt-arr[i] not in second_set:
                second_set.update([crnt-arr[i]])
    if len(second_set) == 0:
        check = -1
        break
    else:
        for key in second_set:
            pre_arr = list(second_set)
if check == 0:
    print(max(pre_arr))
else:
    print(-1)
