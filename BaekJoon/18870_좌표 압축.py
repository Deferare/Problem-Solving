from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dict = {}

for i in range(n):
    if arr[i] in dict:
        dict[arr[i]].append(i)
    else:
        dict[arr[i]] = [i]

keys = list(set(dict))
keys.sort()
value = 0

for key in keys:
    for crnt2 in dict[key]:
        arr[crnt2] = value
    value += 1
    
print(*arr)
