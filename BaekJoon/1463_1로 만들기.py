n = int(input())
memo = [-1 for _ in range(n+10)]
memo[1] = 0
memo[2] = 1
memo[3] = 1

if n <= 3:
    print(memo[n])
else:
    for number in range(4, n + 1):
        a = n+1000005
        b = n+1000005
        if number % 3 == 0:
            push = int(number / 3)
            a = memo[push]
        if number % 2 == 0:
            push = int(number / 2)
            b = memo[push]
        memo[number] = min(a, b, memo[number-1]) + 1
    print(memo[n])
