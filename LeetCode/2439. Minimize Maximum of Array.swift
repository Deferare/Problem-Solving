import Foundation

class Solution {
    func minimizeArrayValue(_ nums: [Int]) -> Int {
        var answer = 0, cumValue = 0
        
        for i in 0..<nums.count {
            cumValue += nums[i]
            answer = max(answer, Int(ceil(Double(cumValue) / Double(i + 1))))
        }

        return answer
    }
}
