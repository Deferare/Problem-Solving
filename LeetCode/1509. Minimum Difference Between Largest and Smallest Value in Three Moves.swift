class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        if nums.count < 5 { return 0 }
        
        let nums = nums.sorted()
        var result = Int.max
        
        for i in 0...3 {
            result = min(result, nums[nums.count-4+i] - nums[i])
        }
        
        return result
    }
}
