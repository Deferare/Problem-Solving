class Solution {
func maxProduct(_ nums: [Int]) -> Int {
    if nums.count > 1 {
        var saveMax = nums[0]; var saveMin = nums[0]
        var result = nums[0]
        for i in 1...nums.count-1 {
            let firstResult = saveMin * nums[i]
            let subMin = min(min(saveMin * nums[i], saveMax*nums[i]), nums[i])
            saveMax = max(max(saveMax * nums[i], saveMin*nums[i]), nums[i])
            saveMin = subMin
            let save = max(saveMax, firstResult)
            if save > result {
                result = save
            }
        }
        return result
    }
    return nums[0]
}
}
