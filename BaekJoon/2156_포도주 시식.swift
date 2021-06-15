var n = Int(readLine()!)!
var arr = [Int](repeating: 0, count: n)
for i in 0...n-1 {
    arr[i] = Int(readLine()!)!
}
var memo = [Int](repeating: -1, count: 10001)
func dp(i:Int) -> Int {
    if i < 0 {
        return 0
    }
    else if i == 0 {
        return arr[i]
    }
    if memo[i] != -1 {
        return memo[i]
    }
    memo[i] = max(max(dp(i: i-2) + arr[i], dp(i: i-3) + arr[i-1] + arr[i]), dp(i: i-1))
    return memo[i]
}
print(dp(i: n-1))
