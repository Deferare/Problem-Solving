n = int(input())

dp_arr = []
dp_arr.append(1)
dp_arr.append(2)
dp_arr.append(3)
if n > 3:
    for i in range(3, n):
        number = i + 1
        cacu_log = number ** 0.5
        if cacu_log.is_integer():
            dp_arr.append(1)
        else:
            sub_arr = []
            num = 1
            while True:
                sq_n = num*num
                if sq_n > number:
                    break
                sub_arr.append(dp_arr[i-sq_n])
                num += 1
            dp_arr.append(min(sub_arr)+1)
            
print(dp_arr[n-1])
