N, M = map(int, input().split(":"))

if N%M == 0:
    print(f"{N//M}:{1}")
elif M%N == 0:
    print(f"{1}:{M // N}")
else:
    while True:
        check = 0
        for i in range(2, min(N,M)//2):
            if N % i == 0 and M % i == 0:
                N //= i
                M //= i
                check = 1
                break
        if check == 0:
            break
    print(f"{N}:{M}")
