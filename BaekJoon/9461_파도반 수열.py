n = int(input())
result = [int]
for i in range(n):
    n2 = int(input())
    save_list = [0 for i in range(105)]
    save_list[0] = 1
    save_list[1] = 1
    save_list[2] = 1
    if n2 <= 3:
        result.append(1)
    else:
        for i in range(3, n2):
            save_list[i] = save_list[i - 2] + save_list[i - 3]
        result.append(save_list[n2 - 1])

for i in result:
    if i == int:
        continue
    print(i)
