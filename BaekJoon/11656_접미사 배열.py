suffix_arr = [input()]
for i in range(1, len(suffix_arr[0])):
    suffix_arr.append(suffix_arr[0][i:])
suffix_arr.sort()
for crnt in suffix_arr:
    print(crnt)
