from sys import stdin

n,m = list(map(int, stdin.readline().split(" ")))
matrix_1 = [list(crnt for crnt in stdin.readline().strip()) for _ in range(n)]
matrix_2 = [list(crnt for crnt in stdin.readline().strip()) for _ in range(n)]
result_cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if matrix_1[i][j] != matrix_2[i][j]:
            if i+3 > n or j+3 > m:
                result_cnt = -1
                break
            result_cnt += 1
            for k in range(3):
                for k2 in range(3):
                    if matrix_1[i+k][j+k2] == "0":
                        matrix_1[i+k][j+k2] = "1"
                    else:
                        matrix_1[i+k][j+k2] = "0"
    if result_cnt == -1:
        break
for i in range(n):
    for j in range(m):
        if matrix_1[i][j] != matrix_2[i][j]:
            result_cnt = -1
            break
    if result_cnt == -1:
        break

print(result_cnt)
