from sys import stdin

def find_parent(x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table[x])
    return parent_table[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: parent_table[b] = a
    else: parent_table[a] = b

N, M = map(int, stdin.readline().split())
cities = [list(map(int, stdin.readline().split(" "))) for _ in range(M)]
parent_table = [i for i in range(N + 1)]
cities.sort(key=lambda x:x[2])

pre = 0
result = 0
for a, b, c in cities:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c
        pre = c
        
result -= pre
print(result)
