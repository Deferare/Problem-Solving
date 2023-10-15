class Solution {
    func minimizeSum(_ nums: [Int]) -> Int {
        let nums = nums.sorted(by: >)
        
        return min(nums[0] - nums[nums.count-3], 
                   nums[1] - nums[nums.count-2],
                   nums[2] - nums[nums.count-1])
    }
}
