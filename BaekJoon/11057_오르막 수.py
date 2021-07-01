from sys import stdin

n = int(stdin.readline())

if n == 1:
    print(10)
else:
    first_arr = [1 for _ in range(9)]
    second_arr = [0 for _ in range(9)]
    for _ in range(n - 1):
        second_arr[0] = first_arr[0] + 1
        for i in range(1, 9):
            second_arr[i] = second_arr[i - 1] + first_arr[i]
        first_arr = second_arr.copy()
    print((sum(second_arr) + 1)%10007)
