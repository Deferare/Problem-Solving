from sys import stdin as st

N = int(st.readline())
arr = [list(map(int, st.readline().split(" "))) for _ in range(N)]
arr.sort(key= lambda x:x[0])
for i in range(N):
    print(f"{arr[i][0]} {arr[i][1]}")
