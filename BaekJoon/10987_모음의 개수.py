S = input()
result_cnt = 0
for i in range(len(S)):
    if S[i] == "a" or S[i] == "e" or S[i] == "i" or S[i] == "o" or S[i] == "u":
        result_cnt += 1
print(result_cnt)
