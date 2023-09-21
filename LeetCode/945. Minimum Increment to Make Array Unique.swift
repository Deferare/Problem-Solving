class Solution {
    func minIncrementForUnique(_ nums: [Int]) -> Int {
        var nums = nums.sorted()
        var result = 0
        for i in 1..<nums.count {
            if nums[i] <= nums[i-1] {
                let diff = nums[i-1] - nums[i] + 1
                result += diff
                nums[i] += diff
            }
        }
        
        return result
    }
}
