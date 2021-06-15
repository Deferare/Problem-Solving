var n = Int(readLine()!)!
var memo = [Int](repeating: -1, count: 100)
func dp(i:Int) -> Int {
    if i <= 2 {
        return 1
    }
    if memo[i] != -1 {
        return memo[i]
    }
    memo[i] = dp(i: i-1) + dp(i: i-2)
    return memo[i]
}
print(dp(i: n))
