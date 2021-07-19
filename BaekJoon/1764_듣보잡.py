from sys import stdin

n,m = map(int, stdin.readline().split(" "))
words_n = {stdin.readline().strip():1 for _ in range(n)}
result_arr = []
for _ in range(m):
    word = stdin.readline().strip()
    if word in words_n:
        result_arr.append(word)
result_arr.sort()

print(len(result_arr))
for crnt in result_arr:
    print(crnt)
