a,b,c = map(int,input().split())
if a < 0 or b>=c:
    print("-1")
else:
    i = a/(c-b)
    print(int(i+1))
