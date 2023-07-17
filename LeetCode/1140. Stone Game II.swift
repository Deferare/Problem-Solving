class Solution {
    func stoneGameII(_ piles: [Int]) -> Int {
        let n = piles.count
        if n == 1 { return piles[0]}
        
        var pilesSum = Array(repeating: 0, count: n)
        pilesSum[n-1] = piles[n-1]
        
        for i in stride(from: n-2, through: 0, by: -1){
            pilesSum[i] = piles[i] + pilesSum[i+1]
        }
        
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        
        for i in stride(from: n-1, through: 0, by: -1){
            for m in stride(from: n-1, through: 0, by: -1){
                for x in 1..<((m * 2) + 1){
                    if i + x < n{
                        dp[i][m] = max(dp[i][m], pilesSum[i] - dp[i+x][max(m, x)])
                    }else{
                        dp[i][m] = max(dp[i][m], pilesSum[i])
                    }
                }
            }
        }
        
        return dp[0][1]
    }
}
