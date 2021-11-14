S = input()
result = "I love UCPC"
byS = "UCPC"
start_index = 0
for i in range(4):
    check = 0
    for j in range(start_index, len(S)):
        if S[j] == byS[i]:
            start_index = j
            check = 1
            break
    if check == 0:
        result = "I hate UCPC"
        break
print(result)
