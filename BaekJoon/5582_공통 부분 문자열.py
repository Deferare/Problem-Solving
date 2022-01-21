A = input()
B = input()
memo = [0 for _ in range(len(A))]
result = 0
for i in range(len(B)):
    memo2 = []
    for j in range(len(A)):
        if B[i] == A[j]:
            if j != 0:
                memo2.append(memo[j-1] + 1)
            else: memo2.append(1)
            result = max(result, memo2[-1])
        else: memo2.append(0)
    memo = memo2
print(result)
