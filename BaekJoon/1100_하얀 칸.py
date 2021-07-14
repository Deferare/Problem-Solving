arr = [input() for _ in range(8)]
check = 0
for i in range(1,9):
    bias = 1
    if i%2 != 0:
        bias = 0
    for j in range(1+bias, 9, 2):
        if arr[i-1][j-1] == "F":
            check += 1
print(check)
