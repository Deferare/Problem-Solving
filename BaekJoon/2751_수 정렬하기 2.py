from sys import stdin

# 입력
n = int(input())
arr = [int(stdin.readline()) for _ in range(n)]
def mergeSort(indexo_1, indexo_2):
    if indexo_2 == indexo_1:
        return [arr[indexo_1]]
    if indexo_2 - indexo_1 == 1:
        if arr[indexo_1] > arr[indexo_2]:
            return [arr[indexo_2], arr[indexo_1]]
        else:
            return [arr[indexo_1], arr[indexo_2]]

    index_half = indexo_1+int((indexo_2-indexo_1)/2)
    arr_left = mergeSort(indexo_1, index_half)
    arr_right = mergeSort(index_half+1, indexo_2)

    arr_left_len = len(arr_left)
    arr_right_len = len(arr_right)
    result_arr = []
    index_left = 0; index_right = 0
    while True:
        if index_left > arr_left_len-1:
            for i in range(index_right, arr_right_len):
                result_arr.append(arr_right[i])
            break
        if index_right > arr_right_len-1:
            for i in range(index_left, arr_left_len):
                result_arr.append(arr_left[i])
            break
        if arr_left[index_left] < arr_right[index_right]:
            result_arr.append(arr_left[index_left])
            index_left += 1
        else:
            result_arr.append(arr_right[index_right])
            index_right += 1
    return result_arr

for crnt in mergeSort(0, n-1):
    print(crnt)
