def cacuRecursion(arr):
    arr[1] += 1
    if arr[0] >= b:
        return arr
    cacu_1 = arr[0]*2
    cacu_2 = int(str(arr[0])+"1")
    arr1 = arr.copy()
    arr1[0] = cacu_1
    arr1 = cacuRecursion(arr1)
    if arr[0] != b:
        arr2 = arr.copy()
        arr2[0] = cacu_2
        arr2 = cacuRecursion(arr2)
        if arr2[0] == b:
            return arr2
    return arr1
a,b = map(int, input().split(" "))
arr = [a,0]
result = cacuRecursion(arr)
if result[0] == b:
    print(result[1])
else:
    print(-1)
