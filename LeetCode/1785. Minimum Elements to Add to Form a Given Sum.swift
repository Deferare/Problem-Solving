class Solution {
    func minElements(_ nums: [Int], _ limit: Int, _ goal: Int) -> Int {
        let sum = nums.reduce(0, +)
        let diff = abs(goal - sum)
        
        return (diff + limit - 1)/limit
    }
}
