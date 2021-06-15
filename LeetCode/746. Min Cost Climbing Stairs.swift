class Solution {
func minCostClimbingStairs(_ cost: [Int]) -> Int {
    var memo = [Int](repeating: -1, count: cost.count+1)
    
    func dp(_ cost:[Int],_ index:Int) -> Int {
        if index == 0 {
            return cost[0]
        }
        else if index < 0 {
            return 0
        }
        
        var value = 0
        if index != cost.count {
            value = cost[index]
        }
        
        if memo[index] != -1 {
            return memo[index]
        }
        memo[index] = min(dp(cost, index-1), dp(cost, index-2)) + value
        return memo[index]
    }
    
    let result = dp(cost, cost.count)
    return result
}
}
