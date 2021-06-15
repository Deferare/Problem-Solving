class Solution {
func findPeakElement(_ nums: [Int]) -> Int {
    if nums.count == 1 {
        return 0
    }
    else {
        func dp(nums:[Int], i:Int) {
            if i >= 0 || i <= nums.count-1{
                if i == 0 && nums[i] > nums[i+1]{
                    result = i
                }
                else if i == nums.count-1 && nums[i] > nums[nums.count-2]{
                    result = i
                }
                else {
                    if nums[i] > nums[i+1] && nums[i] > nums[i-1] {
                        result = i
                    }
                    else {
                        dp(nums: nums, i: i+1)
                    }
                }
            }
        }
        var result = 0
        dp(nums: nums, i: 0)
        return result
    }
}
}
