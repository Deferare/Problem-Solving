from sys import stdin
import sys
sys.setrecursionlimit(100000)
N, M = map(int, stdin.readline().split(" "))
matrix = list(list(map(int, stdin.readline().split(" "))) for _ in range(N))
arr = list(list(-1 for _ in range(M)) for _ in range(N))
def dp(ind_1, ind_2, pre_v):
    if ind_1 >= N or ind_2 >= M or ind_1 < 0 or ind_2 < 0: return 0
    if ind_1 == N - 1 and ind_2 == M - 1:
        if matrix[ind_1][ind_2] < pre_v: return 1
        return 0
    if matrix[ind_1][ind_2] >= pre_v or arr[ind_1][ind_2] == 0: return 0
    if arr[ind_1][ind_2] != -1: return arr[ind_1][ind_2]
    arr[ind_1][ind_2] = 0
    arr[ind_1][ind_2] = dp(ind_1 + 1, ind_2, matrix[ind_1][ind_2]) +\
                        dp(ind_1, ind_2 + 1, matrix[ind_1][ind_2]) +\
                        dp(ind_1 - 1, ind_2, matrix[ind_1][ind_2]) +\
                        dp(ind_1, ind_2 - 1, matrix[ind_1][ind_2])
    return arr[ind_1][ind_2]
print(dp(0, 0, 10001))
