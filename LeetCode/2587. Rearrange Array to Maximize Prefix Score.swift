class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted(by: >)
        
        var prefixSum: Int = 0
        var positiveCount: Int = 0
        
        for num in sortedNums {
            prefixSum += num
            if prefixSum > 0 {
                positiveCount += 1
            } else {
                break
            }
        }
        
        return positiveCount
    }
}
