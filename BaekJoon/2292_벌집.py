n = int(input())

save_num = 1
add_num = 0
cnt = 2

if n == 1:
    cnt = 1
elif n < 8:
    cnt = 2
else:
    if n == 8:
        cnt = 3
    else:
        while True:
            add_num += 6
            save_num += add_num
            # print("add_num : ", add_num)
            # print("save_num : ", save_num)
            # print("cnt : ", cnt)
            # print()
            if save_num >= n:
                # cnt += 1
                break
            cnt += 1

print(cnt)
