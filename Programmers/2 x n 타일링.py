def solution(n):
    if n == 1:
        return 1
    arr = [1,2]
    for _ in range(2,n):
        arr.append(arr[0]+arr[1])
        arr.pop(0)
    return arr[-1]%1000000007
