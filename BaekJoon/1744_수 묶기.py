from sys import stdin

n = int(stdin.readline())
arr_minus = []
arr_plush = []
for _ in range(n):
    push = int(stdin.readline())
    if push > 0:
        arr_plush.append(push)
    else:
        arr_minus.append(push)
arr_minus.sort(reverse=True)
arr_plush.sort()
for i in range(len(arr_plush)):
    arr_minus.append(arr_plush[i])
result = 0
index = n-1
while index >= 0:
    if index == 0:
        result += arr_minus[index]
    else:
        if arr_minus[index]*arr_minus[index-1] > arr_minus[index]+arr_minus[index-1]:
            result += arr_minus[index]*arr_minus[index-1]
            index -= 1
        else:
            result += arr_minus[index]
    index -= 1
print(result)
