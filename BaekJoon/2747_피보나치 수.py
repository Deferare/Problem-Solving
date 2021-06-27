n = int(input())

first_n = 1
second_n = 1
main_n = 0

if n <= 2:
    print(1)
else:
    for _ in range(n - 2):
        main_n = first_n + second_n
        first_n = second_n
        second_n = main_n
    print(main_n)
