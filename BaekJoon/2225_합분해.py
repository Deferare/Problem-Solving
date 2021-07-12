n,k = map(int, input().split(" "))

first_arr = [i for i in range(1, k+1)]
second_arr = [0 for i in range(k)]
second_arr[0] = 1
for i in range(n-1):
    for j in range(1, k):
        second_arr[j] = second_arr[j-1] + first_arr[j]
    first_arr = second_arr.copy()

print(first_arr[k-1]%1000000000)
