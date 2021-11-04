from sys import stdin
test_case = int(stdin.readline())
for i in range(test_case):
    x, y = map(int, stdin.readline().split())
    d = y - x
    n = 0
    while True:
        if d <= n*(n+1):
            break
        n += 1
    if d <= n**2:
        print(n*2-1)
    else:
        print(n*2)
