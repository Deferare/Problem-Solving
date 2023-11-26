class Solution {
    func firstMissingPositive(_ nums: [Int]) -> Int {
        var nums = nums
        let n = nums.count

        for i in 0..<n {
            while nums[i] > 0 && nums[i] < n && nums[i] != nums[nums[i] - 1] {
                nums.swapAt(i, nums[i] - 1)
            }
        }
        
        for i in 0..<n {
            if nums[i] != i+1 {
                return i + 1
            }
        }
        
        return n + 1
    }
}
