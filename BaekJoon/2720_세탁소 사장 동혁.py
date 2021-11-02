from sys import stdin
n = int(stdin.readline())
for _ in range(n):
    change = int(stdin.readline())
    if change >= 25:
        print(change // 25, end=" ")
        change = change % 25
    else:
        print("0", end=" ")
    if change >= 10:
        print(change // 10, end=" ")
        change = change % 10
    else:
        print("0", end=" ")
    if change >= 5:
        print(change//5, end=" ")
        change = change%5
    else:
        print("0", end=" ")
    if change >= 1:
        print(change//1)
    else:
        print("0")
