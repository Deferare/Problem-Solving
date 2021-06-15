class Solution {
func coinChange(_ coins: [Int], _ amount: Int) -> Int {
    var memo = [Int](repeating: -1, count: amount+1)
    func dp(coins:[Int], amount:Int) -> Int {
        if amount == 0 {
            return 0
        }
        if memo[amount] != -1 {
            return memo[amount]
        }
        var min = amount+100000
        for i in 0...coins.count-1 {
            if amount-coins[i] >= 0 {
                var value = amount+amount
                value = dp(coins: coins, amount: amount-coins[i])
                if value < min {
                    min = value
                }
            }
        }

        if min == amount+100000 {
            return amount+100000
        }
        min += 1
        memo[amount] = min
        return memo[amount]
    }
    let value = dp(coins: coins, amount: amount)
    if value >= amount+10000 {
        return -1
    }
    return value
}
}
