import sys

n = int(sys.stdin.readline())
first = 0
second = 1
main_value = 0
for i in range(n-1):
    main_value = first + second
    first = second
    second = main_value
print(main_value, end="")
