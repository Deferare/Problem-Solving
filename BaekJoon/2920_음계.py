arr = list(map(int, input().split()))

result = "mixed"
check = 0
if arr[0] == 1:
    for i in range(1,8):
        if arr[i] != i+1:
            print(result)
            check = 1
            break
    if check == 0:
        print("ascending")

elif arr[0] == 8:
    for i in range(1,8):
        if arr[i] != 8-i:
            print(result)
            check = 1
            break
    if check == 0:
        print("descending")
else:
    print(result)
