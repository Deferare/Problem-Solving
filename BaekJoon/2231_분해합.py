n = int(input())

result = 0
for i in range(1, n+1):
    sum = i
    str_sub = str(i)
    for crnt in str_sub:
        sum += int(crnt)
    if sum == n:
        result = i
        break
print(result)
