from collections import deque
from sys import stdin
n = int(input())
q = deque()
for _ in range(n):
    order = stdin.readline().strip()
    if order[0] == "p":
        if order[1] == "u":
            a, b = map(str, order.split(" "))
            if order[5] == "f":
                q.appendleft(b)
            else:
                q.append(b)
        else:
            if len(q) == 0:
                print("-1")
            elif order[4] == "f":
                print(q.popleft())
            else:
                print(q.pop())
    elif order[0] == "s":
        print(len(q))
    elif order[0] == "e":
        if len(q) == 0:
            print("1")
        else:
            print("0")
    elif order[0] == "f":
        if len(q) == 0:
            print("-1")
        else:
            print(q[0])
    else:
        if len(q) == 0:
            print("-1")
        else:
            print(q[-1])
