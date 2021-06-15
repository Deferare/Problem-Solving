class Solution {
func change(_ amount: Int, _ coins: [Int]) -> Int {
    if amount == 0 {
        return 1
    }
    if amount != 0 && coins.count == 0 {
        return 0
    }
    if coins.count == 1 && amount%coins[0] == 0 {
        return 1
    }
    else if coins.count == 1 && amount%coins[0] != 0 {
        return 0
    }
    
    var dp = [Array](repeating: [Int](repeating: 0, count: amount+1), count: coins.count+1)
    for i in 0...amount {
        if amount%coins[0] == 0 {
            dp[1][i] = 1
        }
    }
    for i in 0...coins.count {
        dp[i][0] = 1
    }
    for i in 1...coins.count {
        for j in 1...amount {
            var add = 0
            if j >= coins[i-1] {
                add = dp[i][j-coins[i-1]]
            }
            dp[i][j] = dp[i-1][j] + add
        }
    }
    return dp[coins.count][amount]
}
}
