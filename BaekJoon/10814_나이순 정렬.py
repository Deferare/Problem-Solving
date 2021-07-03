from sys import stdin

n = int(stdin.readline())

dict = {}

for _ in range(n):
    a,b = stdin.readline().split()
    if int(a) in dict:
        dict[int(a)].append(b)
    else:
        dict[int(a)] = [b]

keys = list(set(dict))
keys.sort()

for key in keys:
    for crnt in dict[key]:
        print(str(key) + " " + crnt)
