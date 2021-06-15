let input = readLine()!.split(separator: " ").map {Int($0)!}
var arr = [Array](repeating: [Int](repeating: 0, count: input[1]), count: input[0])
for i in 0...arr.count-1 {
    let putSave = readLine()!.split(separator: " ").map {Int($0)!}
    for j in 0...putSave.count-1 {
        arr[i][j] = putSave[j]
    }
}
var memo = [Array](repeating: [Int](repeating: -1, count: 1005), count: 1005)
func dp(i:Int, j:Int) -> Int {
    if i >= arr.count || j >= arr[i].count {
        return 0
    }
    if memo[i][j] != -1 {
        return memo[i][j]
    }
    memo[i][j] = max(max(dp(i: i+1, j: j), dp(i: i, j: j+1))+arr[i][j], dp(i: i+1, j: j+1))
    return  memo[i][j]
}
print(dp(i: 0, j: 0))
