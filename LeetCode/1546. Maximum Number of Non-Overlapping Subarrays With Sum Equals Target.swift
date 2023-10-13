class Solution {
    func maxNonOverlapping(_ nums: [Int], _ target: Int) -> Int {
        var seen: Set<Int> = [0]
        var cumSum = 0, count = 0
        
        for num in nums {
            cumSum += num
            if seen.contains(cumSum - target) {
                count += 1
                seen.removeAll()
            }
            seen.insert(cumSum)
        }
        
        return count
    }
}
