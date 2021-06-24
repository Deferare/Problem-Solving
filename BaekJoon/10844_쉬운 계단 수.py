n = int(input())

arr_first = [1 for _ in range(10)]
arr_second = [0 for _ in range(10)]
if n == 1:
    print(sum(arr_first)-arr_first[0])
else:
    for i in range(1, n):
        arr_second[0] = arr_first[1]
        for j in range(1, 9):
            arr_second[j] = arr_first[j - 1] + arr_first[j + 1]
        arr_second[9] = arr_first[8]
        arr_first = arr_second.copy()
    print((sum(arr_second) - arr_second[0])%1000000000)
