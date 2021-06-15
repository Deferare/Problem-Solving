var n = Int(readLine()!)!
var memo = [Int](repeating: -1, count: 1000002)
func dp(i:Int) -> Int {
    if i <= 2 {
        return i
    }
    if i >= 0 {
        if memo[i] != -1 {
            return memo[i]
        }
    }
    memo[i] = dp(i: i-1) + dp(i: i-2)
    memo[i] %= 15746
    return  memo[i]
}
print(dp(i: n))
