a,b,v = map(int, input().split(" "))
result = -1
vb = v-b
ab = a-b
if vb%ab == 0:
    result = vb/ab
else:
    result = vb/ab+1
print(int(result))
