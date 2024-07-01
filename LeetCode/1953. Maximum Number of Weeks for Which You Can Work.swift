class Solution {
    func numberOfWeeks(_ milestones: [Int]) -> Int {
        let max = milestones.max() ?? 0
        let total = milestones.reduce(0, +)
        
        if max > total - max + 1 {
            return 2 * (total - max) + 1
        }
        
        return total
    }
}
