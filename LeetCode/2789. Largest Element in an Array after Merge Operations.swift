class Solution {
    func maxArrayValue(_ nums: [Int]) -> Int {
        var nums = nums
        
        for i in stride(from: nums.count-1, to: 0, by: -1) {
            if nums[i-1] <= nums[i] {
                nums[i-1] += nums[i]
            }
        }

        return nums.max()!
    }
}
