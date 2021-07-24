from sys import stdin
n = int(stdin.readline())
arr = list(int(stdin.readline()) for _ in range(n))
pre_value = arr[-1]
result_sum = 0
for i in range(2, n+1):
    if arr[-i] >= pre_value:
        sub_cacu = arr[-i]-pre_value+1
        result_sum += sub_cacu
        pre_value = arr[-i]-sub_cacu
    else:
        pre_value = arr[-i]
print(result_sum)
