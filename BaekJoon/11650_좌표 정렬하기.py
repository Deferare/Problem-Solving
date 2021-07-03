from sys import stdin

n = int(stdin.readline())

dict = {}

for _ in range(n):
    a,b = map(int, stdin.readline().split())
    if a in dict:
        dict[a].append(b)
    else:
        dict[a] = [b]
keys = list(set(dict))
keys.sort()
for key in keys:
    dict[key].sort()
    for crnt in dict[key]:
        print(str(key) + " " + str(crnt))
