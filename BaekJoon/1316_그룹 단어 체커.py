num = int(input())
count = 0
for j in range(num):
    a = input()
    chr=[]
    cou = 0
    for i in range(len(a)):
        cou += 1
        if a[i] not in chr:
            chr.append(a[i])
        elif a[i] != a[i-1]:
            break
        if cou == len(a):
            count += 1
print(count)
