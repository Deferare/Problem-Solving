arr = [int(input()) for _ in range(9)]

arr_sum = sum(arr)
check = 0
for i in range(8):
    for j in range(i+1,9):
        crnt = arr_sum - (arr[i] + arr[j])
        if crnt == 100:
            save = []
            for k in  range(9):
                if k != i and k != j:
                    save.append(arr[k])
            save.sort()
            for k in range(7):
                print(save[k], end="")
                if k != 6:
                    print()
            check = 1
            break
    if check == 1:
        break
