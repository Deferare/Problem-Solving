n = int(input())
arr = list(map(int, input().split(" ")))

max_arr = [1]
for i in range(1,n):
    sub_max = 0
    for j in range(i):
        if arr[i] > arr[j] and max_arr[j] > sub_max:
            sub_max = max_arr[j]
    max_arr.append(sub_max+1)
    
print(max(max_arr))
