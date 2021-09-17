def solution(numbers):
    arr = [0,1,2,3,4,5,6,7,8,9]
    for number in numbers:
        arr[number] = 0
    return sum(arr)
