class Solution {
func maxProduct(_ nums: [Int]) -> Int {
    var max1 = 0; var max2 = 0
    for i in 0...nums.count-1 {
        if nums[i] >= max1 {
            max2 = max1
            max1 = nums[i]
        }
        else if nums[i] > max2 && nums[i] < max1 {
            max2 = nums[i]
        }
    }
    return (max1-1)*(max2-1)
}
}
