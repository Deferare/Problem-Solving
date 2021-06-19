n = int(input())
arr = list(map(int, input().split(" ")))
stact = []
result = []

for i in range(1, n+1):
    while True:
        if len(stact) == 0:
            result.append("-1")
            stact.append(arr[-i])
            break
        else:
            if arr[-i] < stact[-1]:
                result.append(str(stact[-1]))
                stact.append(arr[-i])
                break
            elif arr[-i] >= stact[-1]:
                stact.pop()

result2 = ""
for i in range(1, n+1):
    result2 += result[-i]
    if i != n:
        result2 += " "
print(result2)
