S = input()
words = {"C","A","M","B","R","I","D","G","E"}
result = ""
for i in range(len(S)):
    if S[i] not in words:
        result += S[i]
print(result)
