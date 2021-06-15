var input = readLine()!.split(separator: " ").map {Int($0)!}
var n = input[0]; var k = input[1]; var w = input[2]
var arr = [Array](repeating: [Int](repeating: -1, count: n+w), count: n+w)
arr[0][0] = 1
arr[1][0] = 1
arr[1][1] = 1
if n >= 1 {
    for i in 2...n+w-2 {
        for j in 0...i {
            if j == 0 || j == i {
                arr[i][j] = 1
            }
            else {
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            }
        }
    }
}
var sum = 0
var index = k-1
for i in n-1...n-1+w-1 {
    for j in k-1...index {
        sum += arr[i][j]
    }
    index += 1
}
print(sum)
