n = int(input())
if n <= 3:
    print(n)
else:
    dp_arr = [i for i in range(1, 4)]
    sqr_arr = []
    sqr_check = {}
    for i in range(1, int(n**0.5)+2):
        sqr_arr.append(i*i)
        sqr_check[i*i] = 1
    for i in range(3, n):
        if i+1 in sqr_check:
            dp_arr.append(1)
        else:
            sub_min = dp_arr[-(sqr_arr[0])]
            index = 0
            dp_arr_len = len(dp_arr)
            while sqr_arr[index] < dp_arr_len:
                if dp_arr[-(sqr_arr[index])] < sub_min:
                    sub_min = dp_arr[-(sqr_arr[index])]
                index += 1
            dp_arr.append(sub_min+1)

    print(dp_arr[-1])
