from sys import stdin

a, b = map(int, stdin.readline().strip().split(' '))

for _ in range(b):
    save = ""
    for _ in range(a):
        save += "*"
    print(save)
