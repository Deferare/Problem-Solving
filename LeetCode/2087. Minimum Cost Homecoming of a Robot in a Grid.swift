class Solution {
    func minCost(_ startPos: [Int], _ homePos: [Int], _ rowCosts: [Int], _ colCosts: [Int]) -> Int {
        return moveCost(startPos[0], homePos[0], rowCosts) + moveCost(startPos[1], homePos[1], colCosts)
    }
    
    private func moveCost(_ start: Int, _ end: Int, _ costs: [Int]) -> Int {
        var cost = 0
        if start < end {
            for i in start+1...end { cost += costs[i] }
        } else if start > end {
            for i in stride(from: start-1, through: end, by: -1) { cost += costs[i] }
        }
        return cost
    }
}
