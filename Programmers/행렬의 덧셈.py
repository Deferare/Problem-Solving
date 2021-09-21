def solution(arr1, arr2):
    result_arr = []
    for i in range(len(arr1)):
        sub_arr = []
        for j in range(len(arr1[i])):
            sub_arr.append(arr1[i][j]+arr2[i][j])
        result_arr.append(sub_arr)
    return result_arr
