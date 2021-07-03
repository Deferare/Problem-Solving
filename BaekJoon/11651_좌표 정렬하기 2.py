from sys import stdin

n = int(stdin.readline())

dict = {}

for _ in range(n):
    a,b = map(int, stdin.readline().split())
    if b in dict:
        dict[b].append(a)
    else:
        dict[b] = [a]
keys = list(set(dict))
keys.sort()
for key in keys:
    dict[key].sort()
    for crnt in dict[key]:
        print(str(crnt) + " " + str(key))
