var n = Int(readLine()!)!
var arr = [Int](repeating: 0, count: 90)
arr[0] = 4
arr[1] = 6
var result = 0
if n <= 2 {
    if n == 1 {
        result = arr[0]
    }
    if n == 2 {
        result = arr[1]
    }
}
else {
    for i in 2...n-1 {
        arr[i] = arr[i-1] + arr[i-2]
    }
    result = arr[n-1]
}
print(result)
