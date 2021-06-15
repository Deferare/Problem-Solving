class Solution {
func maxSubArray(_ nums: [Int]) -> Int {
    if nums.count > 1 {
        var arr = [Int](repeating: 0, count: nums.count)
        arr[0] = nums[0]
        var max = nums[0]
        for i in 1...nums.count-1 {
            let save = nums[i] + arr[i-1]
            if save > nums[i] {
                arr[i] = save
            }
            else {
                arr[i] = nums[i]
            }
            if arr[i] > max {
                max = arr[i]
            }
        }
        return max
    }
    return nums[0]
}
}
