n = list(map(str,input()))
s = 0
for i in range(len(n)):
    s += int(n[i])
if s%3 == 0:
    n.sort(reverse=True)
    if n[-1] == "0":
        for i in range(len(n)):
            print(n[i], end="")
    else:
        print(-1)
else:
    print(-1)
