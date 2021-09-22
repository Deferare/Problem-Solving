def solution(cookie):
    left_arr = [[cookie[0]]]
    for i in range(1, len(cookie)):
        new_arr = [cookie[i]]
        for j in range(len(left_arr[i-1])):
            new_arr.append(left_arr[i-1][j]+cookie[i])
        left_arr.append(new_arr)
    right_arr = [{cookie[-1]}]
    for i in range(2, len(cookie)+1):
        new_arr = {cookie[-i]}
        for pre_value in right_arr[0].intersection():
            new_arr.add(pre_value+cookie[-i])
        right_arr.insert(0, new_arr)
    result_max = 0
    for i in range(len(left_arr)-1):
        for j in range(len(left_arr[i])):
            if left_arr[i][j] in right_arr[i+1]:
                if left_arr[i][j] > result_max:
                    result_max = left_arr[i][j]
    return result_max
