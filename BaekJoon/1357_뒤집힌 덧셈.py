X,Y = map(str, input().split(" "))
x = ""
for i in range(1,len(X)+1):
    x += X[-i]
y = ""
for i in range(1,len(Y)+1):
    y += Y[-i]
result_sub = str(int(x)+int(y))
result = ""
for i in range(1, len(result_sub)+1):
    result += result_sub[-i]
print(int(result))
