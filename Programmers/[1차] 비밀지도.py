def solution(n, arr1, arr2):
    result_arr = []
    for i in range(n):
        bin_sub = bin(arr1[i] | arr2[i])
        sub_arr = []
        for j in range(2, len(bin_sub)):
            if bin_sub[j] == "1":
                sub_arr.append("#")
            else:
                sub_arr.append(" ")
        if len(sub_arr) < n:
            for _ in range(n-len(sub_arr)):
                sub_arr.insert(0, " ")
        result_sub = ""
        for crnt in sub_arr:
            result_sub += crnt
        result_arr.append(result_sub)
    return result_arr
