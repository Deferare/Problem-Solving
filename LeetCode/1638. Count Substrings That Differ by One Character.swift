class Solution {
    func countSubstrings(_ s: String, _ t: String) -> Int {
        let sArray = Array(s)
        let tArray = Array(t)
        let sLength = sArray.count
        let tLength = tArray.count
        
        var dp = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: 2), count: tLength + 1), count: sLength + 1)
        var count = 0
        
        for i in 1...sLength {
            for j in 1...tLength {
                if sArray[i-1] == tArray[j-1] {
                    dp[i][j][0] = dp[i-1][j-1][0] + 1
                    dp[i][j][1] = dp[i-1][j-1][1]
                } else {
                    dp[i][j][1] = dp[i-1][j-1][0] + 1
                }
                count += dp[i][j][1]
            }
        }
        
        return count
    }
}
