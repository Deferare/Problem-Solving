n = int(input())
arr = [0,0,1,1]
for i in range(4, n+1):
    sub_result = arr[i-1]
    if i%2 == 0 and sub_result > arr[int(i/2)]:
        sub_result = arr[int(i/2)]
    if i%3 == 0 and sub_result > arr[int(i/3)]:
        sub_result = arr[int(i/3)]
    arr.append(sub_result+1)
index = n
result_arr = [n]
while len(result_arr) != arr[n]+1:
    result = index-1
    sub_result = arr[index-1]
    if index%2 == 0 and sub_result > arr[int(index/2)]:
        result = int(index/2)
        sub_result = arr[int(index/2)]
    if index%3 == 0 and sub_result > arr[int(index/3)]:
        result = int(index / 3)
        sub_result = arr[int(index/3)]
    result_arr.append(result)
    index = result
print(arr[n])
print(*result_arr)
