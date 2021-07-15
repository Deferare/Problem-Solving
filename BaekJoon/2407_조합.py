n,m = map(int, input().split(" "))

first_arr = []
second_arr = []
first_arr.append(1)
second_arr.append(2)
for i in range(n-1):
    for j in range(i):
        second_arr.append(first_arr[j]+first_arr[j+1])
    first_arr = second_arr.copy()
    first_arr.append(1)
    second_arr = [i+3]

if n == 1:
    print(1)
else:
    print(first_arr[m-1])
