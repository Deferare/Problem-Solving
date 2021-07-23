from sys import stdin
case_check = 1
while True:
    l,p,v = map(int, stdin.readline().split(" "))
    if l == 0 and p == 0 and v == 0:
        break
    if v > p:
        result = l * (v // p)
        result += min(v%p, l)
    else:
        result = v
    print(f"Case {case_check}: {result}")
    case_check += 1
