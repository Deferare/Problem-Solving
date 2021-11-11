from sys import stdin
N = int(stdin.readline())
room = [stdin.readline().strip() for _ in range(N)]
bias = 0
result_cnt = 0
for i in range(N):
    j = 0
    while j < N-1:
        if room[i][j] == "." and room[i][j+1] == ".":
            result_cnt += 1
            while j < N-1:
                if room[i][j] != ".":
                    break
                j += 1
        j += 1
print(result_cnt, end=" ")
result_cnt = 0
for j in range(N):
    i = 0
    while i < N-1:
        if room[i][j] == "." and room[i+1][j] == ".":
            result_cnt += 1
            while i < N-1:
                if room[i][j] != ".":
                    break
                i += 1
        i += 1
print(result_cnt)
