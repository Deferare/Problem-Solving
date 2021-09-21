def solution(s):
    arr = list(s.split(" "))
    for i in range(len(arr)):
        new_str = ""
        for j in range(len(arr[i])):
            if j%2 != 0:
                new_str += arr[i][j].lower()
            else:
                new_str += arr[i][j].upper()
        arr[i] = new_str
    result = ""
    for i in range(len(arr)):
        result += arr[i]
        if i < len(arr)-1:
            result += " "
    return result
