var input = readLine()!.split(separator: " ").map {Int($0)!}
var n = input[0]; var k = input[1]
var arr = [Array](repeating: [Int](repeating: -1, count: n+1), count: n+1)
arr[0][0] = 1
arr[1][0] = 1
arr[1][1] = 1
if n > 2 {
    for i in 2...n-1 {
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
print(arr[n-1][k-1])
