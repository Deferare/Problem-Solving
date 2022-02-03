from sys import stdin as st

n, m = map(int, st.readline().split(" "))
arr = [list(map(int, st.readline().split(" "))) for _ in range(m)]
a,b = 1001, 1001
for i in range(m):
    if arr[i][0] < a: a = arr[i][0]
    if arr[i][1] < b: b = arr[i][1]
if n > 6:
    result_1 = a * (n//6)
    if n%6 != 0: result_1 += b * ((n % 6) // 1)
    result_1 = min(result_1, (a * (n//6)) + a)
else:
    result_1 = a * (6//n)
result_2 = b * (n//1)

print(min(result_1, result_2))
