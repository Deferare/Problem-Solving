class Solution {
func moveZeroes(_ nums: inout [Int]) {
    if nums.count > 1 {
        var zeroCheck = 0
        var arr = [Int](repeating: 0, count: nums.count)
        var index = 0
        for i in 0...nums.count-1 {
            if nums[i] == 0 {
                zeroCheck += 1
            }
            else {
                arr[index] = nums[i]
                index += 1
            }
        }
        if zeroCheck > 0 {
            nums = arr
            for i in nums.count-zeroCheck...nums.count-1 {
                nums[i] = 0
            }
        }
    }
}
}
