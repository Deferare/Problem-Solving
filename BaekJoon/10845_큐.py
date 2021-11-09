from collections import deque
from sys import stdin
n = int(input())
q = deque()
for _ in range(n):
    order = stdin.readline().strip()
    if order[1] == "u":
        a,b = map(str, order.split(" "))
        q.append(b)
    elif order[1] == "o":
        if len(q) == 0:
            print("-1")
        else:
            print(q.popleft())
    elif order[1] == "i":
        print(len(q))
    elif order[1] == "m":
        if len(q) == 0:
            print("1")
        else:
            print("0")
    elif order[1] == "r":
        if len(q) == 0:
            print("-1")
        else:
            print(q[0])
    elif order[1] == "a":
        if len(q) == 0:
            print("-1")
        else:
            print(q[-1])
