class Solution {
func uniquePaths(_ m: Int, _ n: Int) -> Int {
    if m == 1 || n == 1{
        return 1
    }
    var dp = [Array](repeating: [Int](repeating: 0, count: n), count: m)
    for i in 0...n-1 {
        dp[m-1][i] = 1
    }
    for i in 0...m-1 {
        dp[i][n-1] = 1
    }
    for i in (0...m-2).reversed() {
        for j in (0...n-2).reversed() {
             dp[i][j] = dp[i][j+1] + dp[i+1][j]
        }
    }
    return dp[0][0]
}
}
